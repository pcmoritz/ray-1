import fcntl
import logging
import os
import ray
import select
import socket
import subprocess
import sys
import termios
import threading

def launch_process(argv):
    launcher = (
"""
import os
import pty
import socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 31337))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn({})
    s.close()
if __name__ == "__main__":
    main()
""").format(argv)
    with open("/tmp/launcher.py", "w") as f:
        f.write(launcher)

    subprocess.Popen(["python", "/tmp/launcher.py"])

@ray.remote
class Proxy:
    def __init__(self, argv, pid):
        logging.disable(level=logging.ERROR)

        self.lock = threading.Lock()
        self.data = b""
        self.out = b""

        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 10000 + pid % 50000))
        self.sock.listen(5)

        # self.process = launch_process(argv)

        self.conn, address = self.sock.accept()

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            writable_fds = []
            with self.lock:
                if self.data:
                    writable_fds += [self.conn]
            r, w, x = select.select([self.conn], writable_fds, [], 0.2)
            with self.lock:
                for fd in w:
                    fd.send(self.data)
                    self.data = b""
                for fd in r:
                    x = fd.recv(8192)
                    self.out += x
                    if x == b"":
                        ray.actor.exit_actor()

    def communicate(self, data):
        with self.lock:
            if data:
                self.data += data
            out = self.out
            self.out = b""
            return out

class PTY:
    def __init__(self, slave=0, pid=os.getpid()):
        # apparently python GC's modules before class instances so, here
        # we have some hax to ensure we can restore the terminal state.
        self.termios, self.fcntl = termios, fcntl

        # open our controlling PTY
        if sys.platform == "linux" or sys.platform == "linux2":
            self.pty  = open(os.readlink("/proc/%d/fd/%d" % (pid, slave)), "rb+", buffering=0)
        else:
            assert sys.platform == "darwin"
            tty = subprocess.check_output("tty").decode().strip()
            self.pty = open(tty, "rb+", buffering=0)

        # store our old termios settings so we can restore after
        # we are finished 
        self.oldtermios = termios.tcgetattr(self.pty)

        # get the current settings se we can modify them
        newattr = termios.tcgetattr(self.pty)

        # set the terminal to uncanonical mode and turn off
        # input echo.
        newattr[3] &= ~termios.ICANON & ~termios.ECHO

        # don't handle ^C / ^Z / ^\
        # newattr[6][termios.VINTR] = b'\x00'
        newattr[6][termios.VQUIT] = b'\x00'
        newattr[6][termios.VSUSP] = b'\x00'

        for i, j in enumerate(newattr[6]):
            newattr[6][i] = ord(j)

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

    def close(self):
        # restore the terminal settings on deletion
        self.termios.tcsetattr(self.pty, self.termios.TCSAFLUSH, self.oldtermios)
        self.fcntl.fcntl(self.pty, self.fcntl.F_SETFL, self.oldflags)

class Shell:
    def __init__(self, argv, pid):
        self.proxy = Proxy.remote(argv, pid)
        self.pty = PTY()

    def communicate(self, inp):
        return ray.get(self.proxy.communicate.remote(inp))
    
    def handle(self):
        data = b""
        while True:
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
            # even if there were no new inputs this round.
            data += self.communicate(b"")

    def close(self):
        self.pty.close()

shell = None

def attach(actor):
    global shell
    logging.disable(level=logging.ERROR)
    actor_id = actor._ray_actor_id.hex()
    pid_data = ray.experimental.internal_kv._internal_kv_get("RAY_ACTOR_{}_PPID".format(actor_id))
    ray.worker._worker_logs_enabled = False
    shell = Shell([], int(pid_data))

def interact(actor):
    global shell
    try:
        shell.handle()
    except Exception as e:
        print("error", e)
        pass
    finally:
        shell.close()

    ray.worker._worker_logs_enabled = True
