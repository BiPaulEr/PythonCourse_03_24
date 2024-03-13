import asyncio
import random

async def worker(label):
    time_to_sleep = random.randint(1, 20)
    print(f"{label} is on")
    await asyncio.sleep(time_to_sleep)
    print(f"{label} is done")
    return label + " has waiting for " + str(time_to_sleep) + " secondes "

async def do_something():
    print("Begin of work")
    for task in asyncio.as_completed((worker("Worker 1"), worker("Worker 2"), worker("Worker 3"), worker("Worker 4"))):
        result = await task
        print(result)

    print("End of work")

print("Main - Starting")
asyncio.run(do_something())
print("Main - Ending")