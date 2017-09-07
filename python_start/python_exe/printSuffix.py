#!/usr/local/bin/python3
#encoding=utf-8
list1 = ['a.xls','b.doc','c.c','d.java','e.js','f.py']
for i in list1:
	print(i[i.rfind('.'):])
