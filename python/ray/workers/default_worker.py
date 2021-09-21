import os
import pty
import select
import socket
import sys
import time
import threading

def background_connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 10000 + os.getpid()))
            break
        except Exception as e:
            print("error", e)
            time.sleep(4.0)

    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)

thread = threading.Thread(target=background_connect, args=())
thread.daemon = True
thread.start()

argv = sys.argv.copy()

argv[0] = argv[0].replace("default_worker.py", "python_worker.py")
pty.spawn(["python"] + argv)
