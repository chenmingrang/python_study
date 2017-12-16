#!/usr/local/bin/python3
import os
import time

#进程中变量互不影
num = 100
ret = os.fork()
if ret == 0:
    print('==== child process ===')
    num += 1
    print('=== child process num=%d ===' % num)
else:
    time.sleep(3)
    print('=== parent process ===')
    print('=== parent process num=%d ===' % num)