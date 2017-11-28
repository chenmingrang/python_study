#有返回值的函数装饰方法
def func(f):
    def func_in(*args, **kw):
        ret = f(*args, **kw)
        return ret

    return func_in

@func
def test1():
    print("==test1==")
    return "hello world"

@func
def test2():
    print("==test2==")

@func
def test3(a, b):
    print("==test3==")
    print("test3 has two args: a = %s; b = %s" % (a, b))

ret1 = test1()
print("test1 return : %s" % ret1)
ret2 =  test2()
print("test2 return : %s" % ret2)

test3(11, 33)