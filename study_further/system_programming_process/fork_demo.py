"""
编写完毕的代码，在没有运行的时候，称之为程序

正在运行着的代码，就成为进程

进程，除了包含代码以外，还有需要运行的环境等，所以和程序是有区别的
"""

#windows 不支持fork，需要在linux环境执行
import os
import time

#程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到子进程中
#然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中是子进程的 id号
ret = os.fork()
if ret==0:
    while True:
        print("===子进程===")
        time.sleep(1)
else:
    while True:
        print("===父进程===")
        time.sleep(1)