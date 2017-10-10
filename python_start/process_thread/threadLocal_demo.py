class Student(object):
    def __init__(self, name, age =27, score=96):
        self.name = name
        self.age = age
        self.score = score
"""
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_1(std)
    do_subtask_2(std)

def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去，传递起来很麻烦
    do_task_1(std)
    do_task_2(std)
"""

import threading

global_dict = {}

def std_thread(name):
    std = Student(name)
    #把std放到全局变量global_dict中；
    global_dict[threading.current_thread()] = std

def do_task_1():
    #不传入std，而是根据当前线程查找；
    std = global_dict[threading.current_thread()]

def do_task_2():
    #任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]

"""
这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑
ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事:
"""

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

print('%s is begining...' % threading.current_thread().name)
t1 = threading.Thread(target=process_thread, args=('Micheal',), name='t1')
t2 = threading.Thread(target=process_thread, args=('James',), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print('%s is ended' % threading.current_thread().name)


"""
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
"""