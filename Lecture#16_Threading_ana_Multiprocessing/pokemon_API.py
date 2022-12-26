import time
import threading
from threading import Thread
import requests
import asyncio
#import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/"
resp = requests.get(f"{BASE_URL}/pokemon")
print(resp)
print(resp.json())

def get_pokemon(number, base_url=BASE_URL):
    try:
        resp = requests.get(f"{BASE_URL}/pokemon/{number}")
        print(f"Name: {resp.json()['name']}")
    except:
        print('Shit happens')

threads = [Thread(target=get_pokemon, args=(number,)) for number in range(20)]
start = time.time()
[t.start() for t in threads];
[t.join() for t in threads];
print(time.time() - start)
