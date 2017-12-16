#!/usr/local/bin/python3
import os

#父进程
ret = os.fork()

if ret == 0:
    #子进程
    print('=== 1 ===')
else:
    #父进程
    print('=== 2 ===')


#父子进程
ret = os.fork()
if ret == 0:
    #孙子进程
    #2儿子
    print('=== 11 ===')
else:
    #父进程
    #儿子
    print('=== 22 ===')