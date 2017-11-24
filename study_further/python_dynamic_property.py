#动态特性
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Micheal', 38)
print(p1.name)
print(p1.age)
#print(p1.addr)#Person' object has no attribute 'addr'
p1.addr = "zhengzhou"
print(p1.addr)

p2 = Person("Tom", 30)
#print(p2.addr)# 'Person' object has no attribute 'addr'

Person.height = 180
#当实例对象没有属性时，会去找类属性
print(p2.height)#180
print(p1.height)#180

class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("====%s is eating=====" % self.name)

def run(self):
    print("====%s is running=====" % self.name)

p3 = Person2("Jim", 25)
"""
    p3.run()#'Person2' object has no attribute 'run'
    #s虽然p3对象中run属性已经指向了run函数，是后来添加的，即p3.run()的时候，并没用把p3当成参数传入函数
    p3.run = run
    p3.run()#TypeError: run() missing 1 required positional argument: 'self'
"""
#给p3对象添加run方法

#方法1
import types
p3.run = types.MethodType(run, p3)#====Jim is running=====
p3.run()

#方法2
# Person2.run = run
# p3.run()#====Jim is running=====

p4 = Person2("Green", 20)
#把p4作为第一个参数传入run方法
func = types.MethodType(run, p4)
func()#====Green is running=====


