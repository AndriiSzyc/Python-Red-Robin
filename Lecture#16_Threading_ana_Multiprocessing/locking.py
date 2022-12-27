import time
import threading
from threading import Thread
import random
import sys

lock = threading.Lock()

# def lock_hogger(lock, sleep=10):
#     print("\t\tThread: Acquiring lock.")
#     lock.acquire()
#     print("\t\tThread: Lock acquired, sleeping")
#     if sleep:
#         time.sleep(sleep)
#     print("\t\tThread: Woke up, releasing lock")
#     lock.release()
# t = Thread(target=lock_hogger, args=(lock, ))
# t.start()

COUNTER = 0
def increment(n, lock):
    global COUNTER
    for _ in range(n):
        lock.acquire()
        COUNTER += 1
        lock.release()
        time.sleep(0.001)
ITERATIONS = 1000
lock = threading.Lock()
threads = [Thread(target=increment, args=(ITERATIONS, lock)) for _ in range(10)]
[t.start() for t in threads];
[t.join() for t in threads];

print(COUNTER == (len(threads) * ITERATIONS))
print(COUNTER, len(threads) * ITERATIONS)
assert COUNTER == (len(threads) * ITERATIONS), f"Invalid value for counter: {COUNTER}"