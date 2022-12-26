import time
import random
import threading
from threading import Thread
import requests

BASE_URL = "http://localhost:5000"
# resp = requests.get(f"{BASE_URL}/price/bitfinex/btc/2020-04-01")
# print(resp)
# print(resp.json())

EXCHANGES = ['bitfinex', 'bitstamp', 'kraken']
# start = time.time()
# for exchange in EXCHANGES:
#     resp = requests.get(f"{BASE_URL}/price/{exchange}/btc/2020-04-01")
#     print(f"{exchange.title()}: ${resp.json()['close']}")
# time.time() - start

def check_price(exchange, symbol, date, base_url=BASE_URL):
    resp = requests.get(f"{base_url}/price/{exchange}/{symbol}/{date}")
    print(f"{exchange.title()}: ${resp.json()['close']}")

#check_price('bitfinex', 'btc', '2020-04-01')

threads = [Thread(target=check_price, args=(exchange, 'btc', '2020-04-01')) for exchange in EXCHANGES]
start = time.time()
[t.start() for t in threads];
[t.join() for t in threads];
print(time.time() - start)