import threading, time

local_school = threading.local()

class Student():
    def __init__(self, name):
        self.name = name


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    time.sleep(0.5)
    process_student()

t1 = threading.Thread(target= process_thread, args=('Micheal',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Tom',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()