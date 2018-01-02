import threading
global_dict = {}

class Student():
    def __init__(self, name):
        self.name = name

def std_thread():
    std = Student("std" + threading.current_thread().getName())
    global_dict[threading.current_thread()] = std
    task1()
    task2()

def task1():
    std = global_dict[threading.current_thread()]
    print("task1:"+std.name)

def task2():
    std = global_dict[threading.current_thread()]
    print("task2:" + std.name)

if __name__ == "__main__":
    for i in range(20):
        t = threading.Thread(target= std_thread)
        t.start()