from multiprocessing import Process, freeze_support
import time

def test():
    for i in range(5):
        print("=== test ===")
        time.sleep(1)

if __name__ == '__main__':
    freeze_support()
    p = Process(target=test)
    p.start()
    print("main process is over.")