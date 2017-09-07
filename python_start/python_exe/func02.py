#!/usr/local/bin/python3
#encoding=utf-8
def sum(a,b,c):
	#print('sum = %d' % (a+b+c))
	return a+b+c

print(sum(1,2,3))

print('='*20)

def f1(*l):
	#一个*，参数被封装成元组
	sum = 0
	for i in l[0]:
		sum = sum + i
	return sum

a = [1,2,3,4,5,6,7,8,9,10]
print('函数定义为f1(*l)')
print('a=',a)
print('f1(a) = %d' % f1(a))
print('='*20)



