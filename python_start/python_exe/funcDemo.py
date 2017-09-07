#!/usr/local/bin/python3
#encoding=utf-8

def displayMenu():
	print('-'*30)
	print('    名片管理系统   v1.0')
	print('1.添加名片')
	print('2.删除名片')
	print('3.修改名片')
	print('4.查询名片')
	print('5.退出系统')
	print('-'*30)

def getChoice():
	selectKey = input('请输入序号：')
	return int(selectKey)

def printList(l):
	for i in l:
		print(i)

nameList = []

i=0
while i<10:
	displayMenu()
	
	key = getChoice()

	if key == 1:
		print('您选择了添加名片功能')
		newName = input('请输入姓名:')
		nameList.append(newName)
		printList(nameList)
	elif key == 2:
		print('您选择了删除名片功能')
		delName = input('请输入要删除的名字：')
		if nameList.count(delName) > 0:
			nameList.remove(delName)
		else:
			print('你输入的名字不存在！！')
		printList(nameList)
	elif key == 5:
		break
	else:
		print('输入有误，请重新选择！')
