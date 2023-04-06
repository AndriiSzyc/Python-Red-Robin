import time
import random
import threading
from threading import Thread
'''class Thread:
    def __init__(self, target, name=None, args=(), kwargs={}):
        pass
(there's a group argument which should be always None, as it's reserved for future use)

In this case, target is the function that will be executed in that particular thread.

Once a thread has been created (instantiated), we'll need to start() it in order for it to begin to process.'''

def simple_worker():
    print('hello', flush=True)
    time.sleep(2)
    print('world', flush=True)

t1 = Thread(target=simple_worker) #created thread
t1.start()
#t1.join() # block all other actions until the thread is finished

print(2+2)