import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")

async def main():
    await hello_world()

# Run the coroutine
asyncio.run(main())