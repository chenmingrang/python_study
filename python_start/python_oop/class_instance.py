class Student(object):
    pass

Tim = Student()
print(Tim)#<__main__.Student object at 0x0000012AC81FD080>

print(Student)#<class '__main__.Student'>

#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性:
Tim.name="Timmy"
print(Tim.name)#Timmy


class Student(object):
    def __init__(self,param):
        self.name = param[0]
        self.score = param[1]

    def print_score(self):
        print('%s : %d' %(self.name,self.score))

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score>=80:
            return 'B'
        else:
            return 'C'


Green = Student(["Green",97])
Green.print_score()#Green : 97
print(Green.score)#97
print(Green.get_grade())#A

#创建Student实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。


"""
和静态语言不同，Python允许对实例变量绑定任何数据，
也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
"""

Tim = Student(["Tim",80])
Tom = Student(["Tom",83])

Tim.age = 28
print(Tim.age)#28

print(Tom.age)#AttributeError: 'Student' object has no attribute 'age'











