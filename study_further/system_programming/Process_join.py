from multiprocessing import Process, freeze_support
import time
import random

def test():
    for i in range(5):
        print("=== num is %d ===" % i)
        time.sleep(1)

if __name__ == '__main__':
    freeze_support()
    p = Process(target=test)
    p.start()
    #等待p结束之后，往下执行
    # p.join()#堵塞
    # p.join(2)#阻塞最长两秒
    time.sleep(random.randint(1, 3))
    p.terminate()#强制终止
    print("main process is over.")