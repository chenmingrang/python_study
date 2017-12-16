import time, threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            print('[%s ]:Micheal is playing!' % self.name)

if __name__ == "__main__":
    for i in range(5):
        t = MyThread()
        t.start()