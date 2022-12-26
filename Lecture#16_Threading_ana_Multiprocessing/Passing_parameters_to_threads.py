import time
import random
import threading
from threading import Thread

'''Passing parameters is simple with the thread constructor, just use the args argument:'''

def simple_worker(time_to_sleep):
    myself = threading.current_thread()
    ident = threading.get_ident()
    print(f"I am thread {myself.name} (ID {ident}), and I'm sleeping for {time_to_sleep}.")
    time.sleep(time_to_sleep)
    print(f'Thread {myself.name} exiting...')

t1 = Thread(target=simple_worker, name='Bubbles', args=(3, ))
t2 = Thread(target=simple_worker, name='Blossom', args=(1.5, ))
t3 = Thread(target=simple_worker, name='Buttercup', args=(2, ))

t1.start()
t2.start()
t3.start()