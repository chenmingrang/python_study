#动态语言：可在运行的过程中，修改代码
#静态语言：编译时已经确定好代码，运行过程中不能修改
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #只允许对Person实例添加name和age属性
    __slots__ = ("name", "age", "addr")

p = Person("Micheal", 29)
print(p.age)
print(p.name)
p.addr = "zhenghzou"
print(p.addr)
#p.score = 100 #AttributeError: 'Person' object has no attribute 'score'
