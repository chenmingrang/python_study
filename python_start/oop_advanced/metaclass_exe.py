class Hello(object):
    def hello(self,name='world'):
        print('Hello, %s' % name)

h = Hello()
h.hello()

print(type(h))#<class '__main__.Hello'>
print(type(Hello))#<class 'type'>


print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

# 先定义函数
def fn(self,name="world"):
    print("Hello %s" % name)

# 创建Hello class
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()#Hello world
print(type(h))#<class '__main__.Hello'>
print(type(Hello))#<class 'type'>

print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

#要创建一个class对象，type()函数依次传入3个参数
"""
1.class的名称
2.继承的父类集合，如果只有一个父类，注意tuple的写法(superclass,)
3.class的方法名称与函数绑定
"""

# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
# 然后调用type()函数创建出class

print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

myLi = MyList()
myLi.add("ssss")
myLi.add("dddd")
print(myLi)#['ssss', 'dddd']
