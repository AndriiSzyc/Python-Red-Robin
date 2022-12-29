import time
import random
import threading
from threading import Thread

'''It's also possible to know the identity of the thread from within the thread itself. 
It might be counter intuitive as we don't have the reference to the created object, 
but the module function threading.currentThread() will provide access to it.'''
def simple_worker():
    sleep_secs = random.randint(1, 5)
    myself = threading.current_thread()
    #print(myself) #<Thread(Bubbles, started 140457768109632)>
    ident = threading.get_ident()
    print(f"I am thread {myself.name} (ID {ident}), and I'm sleeping for {sleep_secs}.")
    time.sleep(sleep_secs)
    print(f'Thread {myself.name} exiting...')

t1 = Thread(target=simple_worker, name='Bubbles')
t2 = Thread(target=simple_worker, name='Blossom')
t3 = Thread(target=simple_worker, name='Buttercup')

t1.start()
t2.start()
t3.start()
print('Waiting...')