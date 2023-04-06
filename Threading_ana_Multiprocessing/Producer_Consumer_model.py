import time
import threading
import random
from threading import Thread
from datetime import datetime, timedelta
import requests
import queue
from queue import Queue

BASE_URL = "http://localhost:5000"
resp = requests.get(f"{BASE_URL}/exchanges")
print(resp)

EXCHANGES = resp.json()
print(EXCHANGES)

START_DATE = datetime(2020, 3, 1)
DATES = [(START_DATE + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(31)]
print(DATES)

resp = requests.get(f"{BASE_URL}/symbols")
print(resp)
SYMBOLS = resp.json()
print(SYMBOLS)

print(len(EXCHANGES) * len(SYMBOLS) * len(DATES))

def check_price(exchange, symbol, date, base_url=BASE_URL):
    resp = requests.get(f"{base_url}/price/{exchange}/{symbol}/{date}")
    return resp.json()

exchange, symbol, date = random.choice(EXCHANGES), random.choice(SYMBOLS), random.choice(DATES)
print(exchange, symbol, date)

work_func = check_price(exchange, symbol, date)
print(work_func)

tasks = Queue()
for exchange in EXCHANGES:
    for date in DATES:
        for symbol in SYMBOLS:
            task = {
                'exchange': exchange,
                'symbol': symbol,
                'date': date,
            }
            #print(task)
            tasks.put(task)

print(tasks.qsize())
print(task)


class PriceResults:
    def __init__(self):
        results = {}
        for exchange in EXCHANGES:
            results[exchange] = {}
            for date in DATES:
                results[exchange][date] = {}
                for symbol in SYMBOLS:
                    results[exchange][date][symbol] = None
        self._results = results

    def put_price(self, price, exchange, symbol, date):
        self._results[exchange][date][symbol] = price

    def get_price(self, exchange, symbol, date):
        return self._results[exchange][date][symbol]

def worker(task_queue, results):
    while True:
        try:
            task = task_queue.get(block=False)
        except queue.Empty:
            print('Queue is empty! My work here is done. Exiting.')
            return
        exchange, symbol, date = task['exchange'], task['symbol'], task['date']
        price = check_price(exchange, symbol, date)
        results.put_price(price, exchange, symbol, date)
        task_queue.task_done()

results = PriceResults()
MAX_WORKERS = 32

threads = [Thread(target=worker, args=(tasks, results)) for _ in range(MAX_WORKERS)]
[t.start() for t in threads];
tasks.join()

for _ in range(5):
    exchange, symbol, date = random.choice(EXCHANGES), random.choice(SYMBOLS), random.choice(DATES)
    price = results.get_price(exchange, symbol, date)
    if price:
        print(f"{exchange.title():<20} price of {symbol.upper():^5} on {date:^10} was: ${round(price['close'], 4):>9}")
    else:
        print(f"No price of {symbol.upper()} for {exchange.title()} on {date}")






