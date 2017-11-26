#类装饰器
class Test(object):
    pass

t= Test()
#t()#TypeError: 'Test' object is not callable

class Test2(object):
    def __call__(self):
        print("====test2====")

t2 = Test2()
t2()#====test2====


print("*="*20, "class decorator", "*="*20)
class Test3(object):
    def __init__(self, func):
       print("===initialize Test3===")
       print("func name is %s " % func.__name__)
       self.__func = func


    def __call__(self, *args, **kwargs):
        print("===func in decorator===")
        self.__func()

#相当于funcTested = Test3(funcTested)
@Test3
def funcTested():
    print("===funcTested decoratoed is called===")

print("**"*15, "funcTested is calling", "**"*15)
funcTested()


