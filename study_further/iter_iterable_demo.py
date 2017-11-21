"""
   可迭代对象
   一类是集合数据类型，如list、tuple、dict、set、str等
   一类是generator，包括生成器和带yield的generator function
   这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
"""
for s in "abc":
    print(s)

#判断是否可以迭代
print("*="*15, 'Iterable', "*="*15)
a = [x for x in range(10)]
b = (x for x in range(10))
print(b)#<generator object <genexpr> at 0x000001C13371F780>
for x in b:
    print(x)

from collections import Iterable
print(isinstance(b, Iterable))#True
print(isinstance({}, Iterable))#True
print(isinstance('string', Iterable))#True
print(isinstance(100, Iterable))#False


#迭代器（可以用next取值的对象）一定可迭代
print("*="*15, 'Iterator', "*="*15)
from collections import Iterator
print(isinstance((x for x in range(10)), (Iterator, )))#True
print(isinstance((x for x in range(10)), (Iterable, )))#True
print(isinstance([], (Iterator, )))#False


print("*="*15, '转化为可迭代对象', "*="*15)
a = [1, 2, 3, 4]
print(type(a))#<class 'list'>
b = iter(a)
print(type(b))#<class 'list_iterator'>
print(isinstance(b, Iterator))#True
print(isinstance(b, Iterable))#True
print(next(b))#1