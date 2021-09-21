import ray

ray.init("auto")

@ray.remote 
class Actor:
    def f(self):
        print("Collecting input:")
        x = input()
        print("Output:", x)

actor = Actor.remote()
actor.f.remote()


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

@ray.remote
class StdinStdoutProxy:
    def __init__(self, pid):
        import os

        self.pid = pid
        self.stdin = open("/proc/{}/fd/0".format(pid), "w")
        self.stdout = open(os.readlink("/proc/{}/fd/1".format(pid)), "rb+")

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        import fcntl
        import termios
        stdin = open("/proc/{}/fd/0".format(pid), "w")
        stdout = open(os.readlink("/proc/{}/fd/1".format(pid)), "rb")
        while True:
            r, w, x = select.select([stdout], [stdin], [])
            print("after select", r, w)
            if r:
                print("r", r[0].read1())
                continue
            for fd in w:
                character = getch()
                if character == "C":
                    return
                if character == "\r":
                    character = "\n"
                fd.write(character)
                fcntl.ioctl(fd, termios.TIOCSTI, character)
                print("u", character)


    def write(self, character):
        import fcntl
        import select
        import termios
        if character:
            stdin.write(character)
            fcntl.ioctl(stdin, termios.TIOCSTI, character)

proxy = StdinStdoutProxy.remote(1353140)
proxy.write.remote("a")
proxy.write.remote("\n")

###

import ray
import select
import socket
import threading

ray.init(log_to_driver=False)
# ray.init()

@ray.remote
class Proxy:
    def __init__(self):
        self.data = b""
        self.out = b""

        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 31337))
        self.sock.listen(5)

        self.conn, address = self.sock.accept()
        print("accepted connection")

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

        print("started thread")

    def run(self):
        import sys
        while True:
            # print("before select")
            writable_fds = []
            if self.data:
                writable_fds += [self.conn]
            r, w, x = select.select([self.conn], writable_fds, [], 0.1)
            # print("after select", r, w)
            for fd in w:
                fd.send(self.data)
                self.data = b""
            for fd in r:
                x = fd.recv(8192)
                self.out += x
                if x == b"":
                    ray.actor.exit_actor()
                print("x", x)

    # def read(self):
    #     return self.sock.read()
    
    # def write(self, data):
    #     self.sock.write(data)

    def communicate(self, data):
        if data:
            self.data += data
        out = self.out
        self.out = b""
        return out

# proxy = Proxy.remote()

###

import os
import termios
import fcntl

class PTY:
    def __init__(self, slave=0, pid=os.getpid()):
        # apparently python GC's modules before class instances so, here
        # we have some hax to ensure we can restore the terminal state.
        self.termios, self.fcntl = termios, fcntl

        # open our controlling PTY
        self.pty  = open(os.readlink("/proc/%d/fd/%d" % (pid, slave)), "rb+", buffering=0)

        # store our old termios settings so we can restore after
        # we are finished 
        self.oldtermios = termios.tcgetattr(self.pty)

        # get the current settings se we can modify them
        newattr = termios.tcgetattr(self.pty)

        # set the terminal to uncanonical mode and turn off
        # input echo.
        newattr[3] &= ~termios.ICANON & ~termios.ECHO

        # don't handle ^C / ^Z / ^\
        newattr[6][termios.VINTR] = b'\x00'
        newattr[6][termios.VQUIT] = b'\x00'
        newattr[6][termios.VSUSP] = b'\x00'

        for i, j in enumerate(newattr[6]):
            if isinstance(newattr[6][i], str):
                newattr[6][i] = ord(j)
            else:
                newattr[6][i] = ord(j.decode())

        # set our new attributes
        termios.tcsetattr(self.pty, termios.TCSADRAIN, newattr)

        # store the old fcntl flags
        self.oldflags = fcntl.fcntl(self.pty, fcntl.F_GETFL)
        # fcntl.fcntl(self.pty, fcntl.F_SETFD, fcntl.FD_CLOEXEC)
        # make the PTY non-blocking
        fcntl.fcntl(self.pty, fcntl.F_SETFL, self.oldflags | os.O_NONBLOCK)

    def read(self, size=8192):
        return self.pty.read(size)

    def write(self, data):
        ret = self.pty.write(data)
        self.pty.flush()
        return ret

    def fileno(self):
        return self.pty.fileno()

    def __del__(self):
        # restore the terminal settings on deletion
        self.termios.tcsetattr(self.pty, self.termios.TCSAFLUSH, self.oldtermios)
        self.fcntl.fcntl(self.pty, self.fcntl.F_SETFL, self.oldflags)

class Shell:
    def __init__(self):
        self.proxy = Proxy.remote()
        self.pty = PTY()

    def communicate(self, inp):
        return ray.get(self.proxy.communicate.remote(inp))
    
    def handle(self):
        data = b""
        while True:
            # print("1")
            writable_fds = []
            if data:
                writable_fds += [self.pty]
            r, w, x = select.select([self.pty], writable_fds, [], 0.1)
            for fd in w:
                fd.write(data)
                data = b""
            for fd in r:
                inp = fd.read(8192)
                data += self.communicate(inp)
            # Maybe read more, this will make sure all output is read
            # even if there were no new inputs
            data += self.communicate(b"")
            # print("2")
        print("Restoring")


try:
    shell = Shell()
    shell.handle()
except:
    del shell.pty
