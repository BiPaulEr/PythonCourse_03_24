import asyncio
import aiofiles
 
async def read_file(file_name):
    async with aiofiles.open(file_name, mode='r') as f:
        contents = await f.read()
        return contents
 
def on_file_processed(task):
    #appellée lorsque fonction terminer, print le result
    result = task.result()
    print(f"{result}")
 
async def worker():
    print("Begin of work")
    taskList = [asyncio.create_task(read_file("file"+str(i)+".txt")) for i in range(1, 4)]
    [task.add_done_callback(on_file_processed) for task in taskList]
    result = await asyncio.gather(*taskList)
    print("End of work")
 
print("Main - Starting")
#planifier lecture fichiers utilisant asyncio.create_task() pour 3 fichiers data/file1.txt
asyncio.run(worker())
print("Main - Ending")