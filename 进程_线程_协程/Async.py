"""
异步编程 笔记

"""

import asyncio

async def func():
    print('begin')
    reponse = await asyncio.sleep(2)
    print('end', reponse)

result = func()

asyncio.run(result)
