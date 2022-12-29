import asyncio
import requests
import aiohttp

BASE_URL = "http://localhost:5000"
EXCHANGES = ['bitfinex', 'bitstamp', 'kraken']
resp = requests.get(f"{BASE_URL}/price/bitfinex/btc/2020-04-01")

async def check_price(swssion, exchange, symbol, date, base_url=BASE_URL):
    #resp = requests.get(f"{base_url}/price/{exchange}/{symbol}/{date}")
    resp = await session.get(f"{base_url}/price/{exchange}/{symbol}/{date}")
    resp_json = await resp.json()
    print(f"{exchange.title()}: ${resp_json['close']}")

# threads = [
#     Thread(target=check_price, args=(exchange, 'btc', '2020-04-01'))
#     for exchange in EXCHANGES
# ]

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[check_price(session, exchange, 'btc', '2020-04-01')for exchange in EXCHANGES])

    print(time.time() - start)
