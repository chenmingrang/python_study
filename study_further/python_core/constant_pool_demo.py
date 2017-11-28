#1.小整数对象池[-5, 257],python 运行时已经创建，不会被垃圾回收
a = -4
b = -4
print(a == b)#True


#============与python控制台结果不一一致！！！===================
#2.大整数对象池，每一个大整数，均创建一个新的对象
m = 1000002
n = 1000002
print(id(m))
print(id(n))


#3.intern机制
a = "hello"
b = "hello"
print(id(a) == id(b))

#有空格等特殊符号为false
m = "hello world"
n = "hello world"
print(id(m) == id(n))
