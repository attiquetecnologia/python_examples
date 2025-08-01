import asyncio
import time

def not_async01():
    print("Not async 01")
    time.sleep(1)

def not_async02():
    print("Not async 02")
    time.sleep(1)

async def async01():
    print("Async 01")
    await asyncio.sleep(1)

async def principal():
    not_async01()
    not_async02()
    tarefa01 = asyncio.create_task(async01())
    await tarefa01

if __name__ == "__main__":
    principal()