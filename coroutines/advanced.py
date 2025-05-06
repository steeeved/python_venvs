import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Started at {time.strftime('%X')}")
    
    # Run sequentially
    await say_after(1, "hello")
    await say_after(2, "world")
    
    # Run concurrently
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    
    await task1
    await task2
    
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())