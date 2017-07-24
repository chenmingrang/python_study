"""
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度
"""

#在Python中，所有数据类型都可以视为对象，当然也可以自定义对象
#自定义的对象数据类型就是面向对象中的类（Class）的概念。

std1 ={'name':'Micheal','score':80}
std2 ={'name':'Green','score':90}

def print_score(std):
    print("%s: %d" % (std['name'],std['score']))

print_score(std1)
print_score(std2)

#这里可以先定义打印的方法，而不需要先有学生信息


class Student:
    def __init__(self,name,score=85):
        self.name = name
        self.score =score

    def print_score(self):
        print('%s:%d' % (self.name,self.score))


Tim = Student('Tim',70)
Tom = Student('Tom')
Tim.print_score()
Tom.print_score()


#面向对象的设计思想是抽象出Class，根据Class创建Instance。
#数据封装、继承和多态是面向对象的三大特点。

