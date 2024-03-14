from threading import Thread
import time 


class WorkerThread(Thread):
    def __init__(self, variable = "*", target = None, name = None, daemon = False):
        super().__init__(daemon = daemon)
        self.variable = variable

    def run(self):
        print(self.name)
        for i in range(0,10):
            print(self.variable, end="", flush=True)
            time.sleep(1)
        print(self.name + " has terminated ")

t1 = WorkerThread("*", target = None, name = "asterix thread", daemon = False)
t2 = WorkerThread(".", target = None, name = "point thread", daemon = False)
t1.start()
time.sleep(5)
t2.start()