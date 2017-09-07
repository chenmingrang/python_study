#!/usr/local/bin/python3
#encoding=utf-8

def printPos(num):
	n = int(num)
	a = n//3
	b = n%3
	print("您的位置是：%d行，%d列" % (a ,b))


num = input("请输入数字：")
printPos(num)
