import time
import random
import threading
from threading import Thread

def simple_worker():
    print('Thread running...')
    time.sleep(5)
    print('Thread finished...')

t = Thread(target=simple_worker)

print(t.is_alive())

t.start()

print(t.is_alive())

t.start() #thread that has finished can't be started again -> raise RuntimeError("threads can only be started once")
