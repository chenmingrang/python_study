#!/usr/local/bin/python3
#encoding=utf-8
num = 100

def f1():
	num = 120
	print(num)

def f2():
	global num
	num = 300
	print(num)

def f3(num):
	num = 400
	print(num)

print(num)
f1()
f2()
print(num)
f3(num)
print(num)
