def outer1(func):
    print("==outer1==")
    def inner1():
        print("==inner1==")
        func()
    return inner1

def outer2(func):
    print("==outer2==")
    def inner2():
        print("==inner2==")
        func()
    return inner2

#只要Python解释器执行到这个代码，那么就会自动的进行装饰，而不是等到调用的时候才进行装饰
@outer1
@outer2
def foo():
    print("==foo==")

#调用foo之前已经完成了装饰
print("*="*15, "foo is called", "*="*15)
foo()