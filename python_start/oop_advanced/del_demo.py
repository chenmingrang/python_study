import sys

class A:
    def __del__(self):
        print("a is deleting.....")

a1 = A()
print(sys.getrefcount(a1))#2 个数加1
a2 = a1
print(sys.getrefcount(a1))#3
a3 = a1
print(sys.getrefcount(a1))#4
del a1#只是删除变量a1
print(sys.getrefcount(a3))#3
del a2#a1和a2为同一个引用,当对象没有引用时，所占内存才会被释放
print(sys.getrefcount(a3))#2
del a3#触发__del__方法
print("*"*20)