#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

import itertools


#count()创建一个无限的迭代器
print('*='*10, 'count', '*='*10)
natuals = itertools.count(1, 3)
for n in natuals:
    if n==10:
        break
    print(n)


#cycle()会把传入的一个序列无限重复下去
print('*='*10, 'cycle', '*='*10)
cs = itertools.cycle('ABC')
n = 1
for c in cs:
    if n == 10:
        break
    print(c)
    n += 1


#repeat()负责把一个元素无限重复下去
print('*='*10, 'repeat', '*='*10)
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

"""
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列:
"""
print('*='*10, 'takewhile', '*='*10)
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, natuals)
print(ns)#<itertools.takewhile object at 0x0000014A0C72A508>
print(list(ns))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
print('*='*10, 'chain', '*='*10)
for c in itertools.chain('ABC', 'XYZ', 'OPQ'):
    print(c)


#groupby()把迭代器中相邻的重复元素挑出来放在一起:
print('*='*10, 'groupby', '*='*10)
for key, group in itertools.groupby('AAABGGGGGGWTTTTAW'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBbbCssSSd', lambda c: c.upper()):
    print(key, list(group))


#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，
# 而是Iterator，只有用for循环迭代的时候才真正计算
