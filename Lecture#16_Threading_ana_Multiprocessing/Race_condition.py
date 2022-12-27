import time
import threading
from threading import Thread
import random
import sys

COUNTER = 0
def increment(n):
    global COUNTER
    for _ in range(n):
        COUNTER += 1
        time.sleep(0.001)

ITERATIONS = 1000
threads = [Thread(target=increment, args=(ITERATIONS,)) for _ in range(10)]
[t.start() for t in threads];

print(COUNTER == (len(threads) * ITERATIONS))
print(COUNTER, len(threads) * ITERATIONS)
assert COUNTER == (len(threads) * ITERATIONS), f"Invalid value for counter: {COUNTER}"