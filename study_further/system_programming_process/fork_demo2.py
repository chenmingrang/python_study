#!/usr/local/bin/python3
import os
import time

ret = os.fork()

if ret == 0:
    print('child--> ===child===')
    time.sleep(1)
    print('child--> parent pid is:%s' % os.getppid())
else:
    print('parent--> ===parent===')
    time.sleep(2)
    print('parent--> child pid is:%s' % ret)
    print('parent--> pid is:%s' % os.getpid())

print('===over===')