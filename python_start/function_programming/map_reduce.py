#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x**2

"""
map()传入的第一个参数是f，即函数对象本身。
由于结果r是一个Iterator，Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。
"""
r=map(f,[1,2,3,4])
print(r)#<map object at 0x00000206375DD080>
print(list(r))#[1, 4, 9, 16]

L=[1,2,3,4,5,6,"gg"]
print(list(map(str,L)))#将数字转化为字符串


#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1]))#1
print(reduce(add,list(range(101))))#5050

L=[1,3,5,7,9]
def fn(x, y):
    return x*10 + y

print("reduce(fn,L)=",reduce(fn,L))#13579

def char2num(s):
    return int(s)

print("reduce(fn,map(char2num,'13579'))=",reduce(fn,map(char2num,'13579')))


def str2int(str):
    def fn(x,y):
        return x*10 +y
    def char2num(s):
        return int(s)
    return reduce(fn,map(char2num,str))

print(str2int('1238960'))#1238960


#lambda函数

def char2num(s):
    return int(s)

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int("234972"))#234972

from string import capwords
def upper(s):
    return capwords(s)

L=['adam', 'LISA', 'barT']
print(list(map(upper,L)))#['Adam', 'Lisa', 'Bart']


L=[1,3,5,7,9]
def fn(x, y):
    return x*y
print('乘积=',reduce(fn,L))#乘积= 945
print('乘积(lambda)=',reduce(lambda x,y:x*y,L))#乘积(lambda)= 945

print(list("abgdc"))#['a', 'b', 'g', 'd', 'c']

import string
def str2double(str):
    pos = len(str)-str.index(".")-1
    #print("pos=",pos)
    str2 = str.replace(".","")
    #print('str2=',str2)
    def f1(x,y):
        return x*10 + y
    def f2(x):
        return int(x)
    return reduce(f1,map(f2,str2))*(10**-pos)

print("str2double('1232.435')=",str2double("1232.435"))