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

def task(n):
    for i in range(1000000):
        change_balance(n)

t1 = threading.Thread(target=task, name="t1", args=(5,))
t2 = threading.Thread(target=task, name="t2", args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
"""
两个线程交互执行：
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
"""



