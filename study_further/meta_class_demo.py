#元类
class Person(object):

    age = 20

    print("====person====test====")

    def __init__(self):
        self.name = "abc"

#类也是对象
print(Person)


print("*="*15, "动态创建类", "*="*15)
def choose_class(name):
    if name == "foo":
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_class("foo")
print(MyClass)#<class '__main__.choose_class.<locals>.Foo'>


print("*="*15, "使用type创建类", "*="*15)
class Test:
    pass
t = Test()
print(type(t))#<class '__main__.Test'>
#type(类名，父类，类属性)
Test2 = type("Test2", (), {})
t2 = Test2()
print(type(t2))#<class '__main__.Test2'>

#type创建class，为元类
Person2 = type("Person2", (), {"age":24})
p2 = Person2()
print("age is %s" % p2.age)#age is 24


def getAge(self):
    print("age = %s" %  self.age)

Person3 = type("Pesron3", (), {"age":24, "getAge":getAge})
p3 = Person3()
p3.getAge()