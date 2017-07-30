#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass

s =Student()
s.name = 'Micheal'
print(s.name)#Micheal

def set_age(self,age):
    self.age = age

from types import MethodType

#还可以尝试给实例绑定一个方法
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)#25

#但是，给一个实例绑定的方法，对另一个实例是不起作用的

s2 = Student()
#s2.set_age(25)#'Student' object has no attribute 'set_age'


#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)#100
s2.set_score(90)
print(s2.score)#90

"""
通常情况下，上面的set_score方法可以直接定义在class中，
但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
"""

#使用__slots__
"""
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
"""

class Student(object):
    __slots__ = ("name","age")

s = Student()
s.name = 'Timmy'
s.age = 30
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#s.score = 99#AttributeError: 'Student' object has no attribute 'score'



####使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99
print(g.score)#99

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

class PrimaryStudent(Student):
    __slots__ = ("score")

p = PrimaryStudent()
p.name = "Tom"
p.age = 30
p.score = 97
#p.addr = "china"#AttributeError: 'PrimaryStudent' object has no attribute 'addr'


















