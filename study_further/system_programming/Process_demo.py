from multiprocessing import Process, freeze_support
import time

def test():
    while True:
        print("=== test ===")
        time.sleep(1)

p = Process(target=test)
p.start()

def test2():
    while True:
        print("=== test2 ===")
        time.sleep(1)

if __name__ == '__main__':
    freeze_support()
    test2()