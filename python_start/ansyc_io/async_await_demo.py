"""
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
"""

import asyncio
import threading

@asyncio.coroutine
def hello():
    print("Thread:%s --> Hello World!" % threading.currentThread())
    r = yield from asyncio.sleep(1)
    print("Thread:%s --> Hello again!" % threading.currentThread())

async def hello2():
    print("Thread:%s --> Hello World!" % threading.currentThread())
    r= await asyncio.sleep(1)
    print("Thread:%s --> Hello again!" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello2(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""Python从3.5版本开始为asyncio提供了async和await的新语法"""

