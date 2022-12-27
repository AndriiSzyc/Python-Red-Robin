import time
import threading
from threading import Thread
import requests
import asyncio
from requests.exceptions import HTTPError

# import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/"
# resp = requests.get(f"{BASE_URL}/pokemon/1")
# print(resp)
# print(resp.json())
# jsonResp = resp.json()
# for key, value in jsonResp.items():
#    print(key, ':', value)
# print(jsonResp['name'], jsonResp['id'])


def get_pokemon(number, lock, base_url=BASE_URL):
    try:
        with lock:
            resp = requests.get(f"{BASE_URL}/pokemon/{number}")
            resp.raise_for_status()
            print(
                f" - Id {resp.json()['id']}. Name: {resp.json()['name']}."
            )

    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exceptions as err:
        print(f"Other error occured: {err}")


lock = threading.Lock()

threads = [Thread(target=get_pokemon, args=(number, lock)) for number in range(1, 21)]
start = time.time()
[t.start() for t in threads]
[t.join() for t in threads]
print(time.time() - start)
