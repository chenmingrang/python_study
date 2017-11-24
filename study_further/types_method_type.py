#实例方法
print("=*"*15, "实例方法", "=*"*15)
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Micheal", 30)

def eat(arg1):
    print("====%s is eating====" % arg1.name)

#p.eat()#AttributeError: 'Person' object has no attribute 'eat'
import types
#p作为第一个参数传递给eat
func = types.MethodType(eat, p)
func()#====Micheal is eating====


#静态方法
print("=*"*15, "静态方法", "=*"*15)
@staticmethod
def test():
    print("====static method====")

Person.test = test
p.test()#====static method====
Person.test()


#类方法
print("=*"*15, "类方法", "=*"*15)
@classmethod
def test2(cls):
    print("class name:%s" % cls.__name__)#class name:Person
    print("====class method====")

Person.test2 = test2
Person.test2()

