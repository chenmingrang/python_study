#给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):
    def __init__(self,name):
        self.name =name

s =Student("Tim")
s.score = 90

print(s.name)#Tim
print(s.score)#90

class Student(object):
    name = "Student"

s = Student()
print(s.name)#Student打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)#Student打印类的name属性

s.name = "Micheal"
print(s.name)#Michael 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)#Student

del s.name
print(s.name)#Student

"""
千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
"""


