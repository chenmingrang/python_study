#带参数的装饰器
from time import ctime, sleep
def func(arg = "hello"):
    def timefun(f):
        def wrapper(*args, **kw):
            print("%s called at %s %s" % (f.__name__, ctime(), arg))
            if arg == "hello":
                f(*args, **kw)
                f(*args, **kw)
            else:
                ret = f(*args, **kw)
                return ret
        return wrapper
    return timefun

#1.先调用func("hello)，这个函数return的结果是func这个函数的引用
#2.@func
#3.使用@func对test进行装装饰
#可以对装饰的逻辑进行处理
@func("hello1")
def test1():
    print("==test1==")
    return "hello world"
test1()

@func("hello")
def test2():
    print("==test2==")
    return "hello world"
test2()