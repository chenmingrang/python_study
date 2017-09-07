#!/usr/local/bin/python3
#encoding=utf-8
i = 1
while i < 10:
	j = 1
	while j <= i:
		print('%d*%d=%-3d' % (i,j,i*j),end=' ')
		j += 1
	i += 1
	print("")
