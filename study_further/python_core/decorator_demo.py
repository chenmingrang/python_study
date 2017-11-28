#装饰器

def foo():
    print("==foo1==")

def foo():
    print("==foo2==")

#下面的会覆盖上面的方法
foo()

def foo1():
    print("==foo1==")

def foo2():
    print("==foo2==")

def foo3():
    print("==foo3==")

def foo4():
    print("==foo4==")


print("*="*15, 'decorator', "*="*15)
#装饰器用闭包实现的
def func(func):
    def inner():
        print("==decorated==")
        func()
    return inner

print("*="*15, 'foo1', "*="*15)
def foo1():
    print("==foo1==")
foo1 = func(foo1)
foo1()

print("*="*15, 'foo2', "*="*15)
@func
def foo2():
    print("==foo2==")
foo2()

print("*="*15, 'foo3', "*="*15)
def foo3():
    print("==foo3==")
foo3()
