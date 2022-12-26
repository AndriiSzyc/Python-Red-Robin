import time
import random
import threading
from threading import Thread

'''So far, the way we've created threads is by passing a target function to be executed. 
There's an alternative, more OOP-way to do it, which is extending the Thread class:'''


class MyThread(Thread):
    def __init__(self, time_to_sleep, name=None):
        super().__init__(name=name)
        self.time_to_sleep = time_to_sleep

    def run(self):
        ident = threading.get_ident()
        print(f"I am thread {self.name} (ID {ident}), and I'm sleeping for {self.time_to_sleep} secs.")
        time.sleep(self.time_to_sleep)
        print(f'Thread {self.name} exiting...')

t = MyThread(2)
t.start()

t2 = MyThread(1.5, 'Bubbles')
t2.start()