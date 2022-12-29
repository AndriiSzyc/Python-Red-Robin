import time
import random
import threading
from threading import Thread

def simple_worker():
    time.sleep(random.random() * 5)  #random number 0 to 1
    value = random.randint(0, 99)    #random number A to B (0 to 99)
    print(f'My value: {value}')

threads = [Thread(target=simple_worker) for _ in range(5)] #created thread

print(threads, type(threads))

[t.start() for t in threads]

#[t.join() for t in threads] # block all other actions until the thread is finished

print(2+2)