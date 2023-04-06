import asyncio
import time
async def some_func():          #step 1 coroutine
    print('Hello ')
    await asyncio.sleep(2)      # not use TIME module
    print('world')

async def main():               #step 2 enter some_func()
    return await some_func()

as_func = asyncio.run(main())   #step 3 call some_func()

print('Hello world')