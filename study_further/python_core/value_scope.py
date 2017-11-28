#变量的作用域
#命名空间（变量的作用范围）

from study_further.python_core.decorator_with_decArgs import test2
test2()

#全局
a = 100

def func():
    # 局部
    b = 100

print(globals())

def func1():
    a = 100
    b = 200
    print(locals())

func1()

#LEGB规则（就近原则）
#locals-->enclosing function(闭包)-->globals-->builtins
num = 100
def func3():
    num = 200
    print(num)#200
func3()

def func4():
    num = 200
    def inner():
        num = 300
        print(num)#300
    return inner
ret = func4()
ret()