import asyncio

async def worker():
    print("Worker is on")
    await asyncio.sleep(2)
    print("Worker has done is work")
    return "The result of worker is heavy to process"

async def do_something():
    print("Begin of work")
    result = await worker()
    print(result)

    result2 = await worker()
    print(result2)
    print("End of work")

print("Main - Starting")
asyncio.run(do_something())
print("Main - Ending")