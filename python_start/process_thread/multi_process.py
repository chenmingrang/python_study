"""
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID
"""
# import os
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just create a child process (%s)' % (os.getpid(), pid))

"""
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求
"""

"""
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象。
"""

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()#等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')
    print('*='*30)


#如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.02f seconds.' % (name,(end-start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)#task 4需在一个进程执行完之后再执行
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess deno...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    # 调用close()之后就不能继续添加新的Process了
    p.close()
    p.join()
    print('All subprocess done.')
    print('*=' * 30)

