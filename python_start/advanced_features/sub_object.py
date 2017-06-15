#取一个li或tuple的部分元素是非常常见的操作
li=['Micheal','Jim','Tom','Green','Tim']

#取前三个元素(常规)
print([li[0],li[1],li[2]])#['Micheal', 'Jim', 'Tom']

#取前n个元素
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(li[0:3])#['Micheal', 'Jim', 'Tom']
#0可以省略
print(li[:3])#['Micheal', 'Jim', 'Tom']
#也可以从其索引开始取
print(li[2:4])#['Tom', 'Green']
#li[-1]取倒数第一个元素
print(li[-1])#Tim
print(li[-2:-1])#['Green']
print(li[-2:])#['Green', 'Tim']
print(li[-2:1])#[]



#example
li=list(range(100))
print(li)
#前10个
print(li[:10])#print(li[0:10])
#后10个
print(li[-10:])
#11-20
print(li[10:20])
#前10个，每两个取一个
print(li[:10:2])#[0, 2, 4, 6, 8]
#10-19每两个取一个
print(li[10:20:2])#[10, 12, 14, 16, 18]
#所有数，每5个取一个：
print(li[::5])#[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#后二十个，每4个取一个
print(li[-20::4])#[80, 84, 88, 92, 96]

#复制(clone)
li1=li[:]#True
print(li1==li)
li1[1]=100
print(li1)
print(li)


#****tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

print((1,2,3,4,5,6)[1::2])#(2, 4, 6)


#****字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print("ABCDEFGHIJKL"[0::2])#ACEGIK

"""
在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
"""


