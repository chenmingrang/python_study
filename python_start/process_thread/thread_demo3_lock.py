"""
多线程和多进程最大的不同在于:
    多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
    而多线程中，所有变量都由所有线程共享，
    所以，任何一个变量都可以被任何一个线程修改，
    因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
"""

import time, threading

balance = 0

def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()

def task(n):
    for i in range(1000000):
        #先获取所对象
        lock.acquire()
        try:
            change_balance(n)
        finally:
            lock.release()

t1 = threading.Thread(target=task, name="t1", args=(5,))
t2 = threading.Thread(target=task, name="t2", args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


"""
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止.
获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放
"""