import time, threading

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1
        print('work1==> g_num is %d...' % g_num)

def work2():
    global g_num
    print('work2==> g_num is %d...' % g_num)

if __name__ == "__main__":
    #线程与线程之间共享全局变量
    #进程与进程之间全局与局部变量各自是各自，互不影响
    t1 = threading.Thread(target=work1)
    t1.start()

    time.sleep(1)

    t2 = threading.Thread(target=work2)
    t2.start()