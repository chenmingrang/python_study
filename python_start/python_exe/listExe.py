#!/usr/local/bin/python3
#encoding=utf-8

import random

def divide(t,o): 
	index = random.randint(0,2)
	for j in t:
		index = random.randint(0,2)
		o[index].append(j)

teachers = ['a','b','c','d','e','f','g','h']
office = [[],[],[]]

while True:
	office = [[],[],[]]
	divide(teachers,office)
	flag = False
	for i in office:
		if len(i)<2:
			flag =True
			break
	if flag:
		continue
	else:
		break


for i in office:
	for j in i:
		print(j)
	print('*'*7)

