import asyncio

async def worker():
    print("Worker is on")
    await asyncio.sleep(2)
    print("Worker has done is work")
    return "The result of worker is heavy to process"

def getTaskInfo(task):
    print("task is cancelled ? ", task.cancelled())
    print("task is done ? ", task.done())
    if (task.done()):
        print("task is result ? ", task.result())
        print("task has exception ? ", task.exception())

def print_result(task):
    print("PRINT RESULT")
    print("task is result ? ", task.result())
    print("task has exception ? ", task.exception())
    print("PRINT RESULT")

async def do_something():
    print("Begin of work")
    task1 = asyncio.create_task(worker()) 
    task1.add_done_callback(print_result)
    #task1.remove_done_callback(print_result)
    getTaskInfo(task1)
    await task1
    getTaskInfo(task1)

    print("End of work")

print("Main - Starting")
asyncio.run(do_something())
print("Main - Ending")
