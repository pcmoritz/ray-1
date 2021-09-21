import os
import pty
import select
import socket
import sys
import time
import threading

with open("/tmp/result.txt", "a") as f:
    f.write("starting")

def background_connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 10000 + os.getpid()))
            break
        except Exception as e:
            print("error", e)
            with open("/tmp/result.txt", "a") as f:
                f.write("X " + str(10000 + os.getpid()))
                f.write("E = " + str(e) + "\n")
            time.sleep(4.0)

    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

with open("/tmp/result.txt", "a") as f:
    f.write("A")

print("X")
thread = threading.Thread(target=background_connect, args=())
print("Y")

with open("/tmp/result.txt", "a") as f:
    f.write("B")

thread.daemon = True

with open("/tmp/result.txt", "a") as f:
    f.write("C")

thread.start()

argv = sys.argv.copy()

with open("/tmp/result.txt", "a") as f:
    f.write("old command, argv = " + str(argv) + "\n")
    f.write("PID = " + str(os.getpid()))

argv[0] = argv[0].replace("default_worker.py", "python_worker.py")

with open("/tmp/result.txt", "a") as f:
    f.write("spawning worker in a pty, argv = " + str(argv) + "\n")

r = pty.spawn(["python"] + argv)

# import subprocess
# r = subprocess.check_call(["python"] + argv)

with open("/tmp/result.txt", "a") as f:
    f.write("result = {}".format(r))