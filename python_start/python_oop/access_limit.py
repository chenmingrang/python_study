'在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑'

#从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %d' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        self.__score = score


#但是已经无法从外部访问实例变量.__name和实例变量.__score了
Tom = Student('Tom',96)
Tom.print_score()#Tom : 96
#print(Tom.__score)#AttributeError: 'Student' object has no attribute '__score'


#这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮
Tom.print_score()#Tom : 96


#通过get和set改变对象的私有属性

Tom.set_name('Tommy')
print(Tom.get_name())#Tommy

Tom.set_score(40)
print(Tom.get_score())#40


"""
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量
"""

print(Tom._Student__name)#Tommy

#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉


"""
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
"""
Tom.__score = 92
print(Tom.__score)#92
print(Tom.get_score())#40

