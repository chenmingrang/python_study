#Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

"""
list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
"""

d = {"a":1,"b":2,"c":3,"d":4}
for key in d:
    print(key,"=",d[key])

#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#遍历值
for value in d.values():
    print(value)

#同时遍历key和value
for item in d.items():
    print("key=",item[0],"value=",item[1])
    #print(type(item))#<class 'tuple'>

#遍历字符串
for ch in "ABCD":
    print(ch)

#****当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

#判断一个对象是否可以替代,通过collection模块的iterable类型来判断

from collections import Iterable
print(isinstance(d,Iterable))#True
print(isinstance("abc",Iterable))#True
print(isinstance([1,2,"2"],Iterable))#True
print(isinstance((1,2,3,4),Iterable))#True
print(isinstance((12345),Iterable))#False
print(isinstance(set([1,2,3,4]),Iterable))#True


# 如果要对list实现类似Java那样的下标循环怎么办?
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身

list = ["a","b","c","d"]
for i,value in enumerate(list):
    str1="list["+str(i)+"]="+value
    print(str1)


#for循环中，同时引用两个变量

for x,y in [{"name":"micheal","age":34},(1,2),[4,5],(44,90)]:
    if isinstance(x,(str)):
        print(333333)#333333
    print(x,y)



