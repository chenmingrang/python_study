#有返回值的函数装饰方法
def func(f):
    print("==func==1==")

    def func_in():
        print("--func_in_before--")
        value = f()
        # print(f.__name__ ,'return value is : %s' % value)
        print("--func_in_after--")
        return value

    print("==func==2==")
    return func_in

@func
def test():
    print("===test===")
    return "hello world"

ret = test()
print("test return value is : %s " % ret)