import time
import random
import threading
from threading import Thread

def simple_worker():
    print('Thread running...')
    time.sleep(5)
    print('Thread exiting...')

t = Thread(target=simple_worker)
print(t.name)  #default name
print(t.ident) #ident will be None until we run the thread.
t.start()
print(t.name)
print(t.ident)

'''We can create a thread and assign a custom name to it:'''
t = Thread(target=simple_worker, name='PyCon 2020 Tutorial!')
t.start()
print(t.name)
print(t.ident)