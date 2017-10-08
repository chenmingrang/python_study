#!/usr/local/bin/python3
#encoding=utf-8
"""
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
"""
#代码在linux上运行
import subprocess

print('$ nslookup www.python.org')
#相当于在linux命令行输入nslookup www.python.org
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)