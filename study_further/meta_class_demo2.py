class Animal:
    def eat(self):
        print("animal %s is eating...." % self.__class__.__name__)

class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()

#动态创建一个类，继承Animal
Cat = type("Cat", (Animal, ), {})
cat1 = Cat()
cat1.eat()


#将类的属性(不改变实例的属性)和方法变为大写
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    newAttr ={}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
        else:
            newAttr[name] = value
    #调用type创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass = upper_attr):
    def __init__(self, name):
        self.name = name

    bar = 'bip'
    def func(self):
        print("test func")

    def __func1(self):
        print("test __func1")

print(hasattr(Foo, 'bar'))#False
print(hasattr(Foo, 'BAR'))#True
foo = Foo('foo')
print(foo.name)#foo
#foo.func()#AttributeError: 'Foo' object has no attribute 'func'
foo.FUNC()#test func
print(dir(foo))

"""
元类的作用（元类是深度的魔法）：
    1.拦截类的创建
    2.修改类
    3.返回修改之后的类
"""