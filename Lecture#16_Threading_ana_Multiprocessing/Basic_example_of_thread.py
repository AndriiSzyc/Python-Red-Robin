import time
import random
import threading
from threading import Thread
import asyncio

def simple_worker():
    print('hello', flush=True)
    time.sleep(2)
    print('world', flush=True)

t1 = Thread(target=simple_worker)
t1.start()
t1.join()