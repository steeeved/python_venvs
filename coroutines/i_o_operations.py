import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, 'r') as f:
        return await f.read()

async def main():
    filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    tasks = [read_file(name) for name in filenames]
    results = await asyncio.gather(*tasks) # runs multiple coroutines concurrently and waits for all to complete.
    for name, content in zip(filenames, results):
        print(f"{name}: {len(content)} characters")

asyncio.run(main()) # runs the main coroutine and manages the event loop (sets up + tears down automatically).