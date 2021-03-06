from threading import Thread
from queue import Queue
import time

class Producer(Thread):

    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 200:
                for i in range(100):
                    count = count + 1
                    msg = "生产产品" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(2.5)

class Consumer(Thread):

    def run(self):
        global queue
        while queue:
            if queue.qsize()>100:
                for i in range(3):
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
                # time.sleep(1)


if __name__ == "__main__":
    queue = Queue()
    for i in range(500):
        queue.put('初始产品' + str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()





