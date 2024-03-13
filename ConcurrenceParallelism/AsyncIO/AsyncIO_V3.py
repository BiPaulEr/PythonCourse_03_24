import asyncio

async def worker():
    print("Worker is on")
    await asyncio.sleep(2)
    print("Worker has done is work")
    return "The result of worker is heavy to process"

async def do_something():
    print("Begin of work")
    result = await asyncio.gather(worker(), worker(), worker(), worker())
    print(result)
    print(type(result))
    print("End of work")

print("Main - Starting")
asyncio.run(do_something())
print("Main - Ending")