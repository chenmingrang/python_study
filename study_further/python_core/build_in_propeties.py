"""
__init__	        构造初始化函数  	    创建实例后,赋值时使用,在__new__后
__new__	            生成实例所需属性	    创建实例时
__class__	        实例所在的类          实例.__class__
__str__	            实例字符串表示,可读性	print(类实例),如没实现，使用repr结果
__repr__	        实例字符串表示,准确性	类实例 回车 或者 print(repr(类实例))
__del__	            析构	                del删除实例
__dict__	        实例自定义属性      	vars(实例.__dict__)
__doc__	            类文档,子类不继承	    help(类或实例)
__getattribute__	属性访问拦截器	        访问实例属性时
__bases__	        类的所有父类构成元素	类名.__bases__
"""

class Player(object):
    def __init__(self, name):
        self.name = name
        self.age = 25

    #属性访问拦截器
    def __getattribute__(self, item):
        print("====1====>%s" % item)
        if item == "age":
            #可以做记录
            print("get age")
            return 20
        #调用父类方法，不要拦截的属性
        else:
            #此处如果访问的为方法，必须这样写，否则返回为None，调用会出错
            #return object.__getattribute__(self, item)
            temp = object.__getattribute__(self, item)
            print("====2====>%s" % str(temp))
            return temp

    def play(self):
        print('%s is playing...' % self.name)

p1 = Player("Michael")
print(p1.name)
print(p1.age)
#p.paly 属性指向了一个函数对象
p1.play()


class Foo(object):
    def __getattribute__(self, item):
        print("-----test------")
        if item == "p1":
            return "hello"
        else:
            #此处不能调用self的方法或是属性，否则会进入死循环
            # return self.test
            return object.__getattribute__(self, item)

    def test(self):
        print("haha")

f =Foo()
print(f.p1)
f.test()