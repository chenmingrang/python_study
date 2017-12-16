from multiprocessing import Process, freeze_support
import time

def test():
    while True:
        print("=== test ===")
        time.sleep(1)

def test2():
    while True:
        print("=== test2 ===")
        time.sleep(1)

#在windows中必须这么写
"""
#在linux中可以这么写
p = Process(target=test)
p.start()

test2()
"""
if __name__ == '__main__':
    freeze_support()
    p = Process(target=test)
    p.start()
    test2()