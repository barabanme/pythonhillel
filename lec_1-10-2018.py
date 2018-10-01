# https://compscicenter.ru/media/slides/python_2015_autumn/2015_12_07_python_2015_autumn_3KfewPJ.pdf

import time
from threading import Thread


# import _thread
import collections

def countdown(n):
    print("Start:", n)
    for i in range(n):
        print(n - i - 1, "left")
        time.sleep(1)
    print("End!")


t = Thread(target=countdown, args=(3,))
t.start()
print("Start S")
s = Thread(target=time.sleep, args=(5,))
s.start()
print("End S")

##############################################################################

import asyncio

async def foo():
    print("Running foo()")
    await asyncio.sleep(0)
    print("End of foo()")

async def bar():
    print("Running bar()")
    await asyncio.sleep(2)
    print("End of bar()")

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_task = asyncio.wait(tasks)
ioloop.run_until_complete(wait_task)
ioloop.close()
