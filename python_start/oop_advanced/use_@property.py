#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数

class Student(object):
    def get_score(self):
        return self.score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be int")
        if value < 0 or value >100:
            raise ValueError("score must between 0 and 100")
        self.score = value

s = Student()
s.set_score(98)
#s.set_score(102)#ValueError: score must between 0 and 100
print(s.get_score())
#s.set_score("100")#ValueError: score must be int
print(s.get_score())

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be int")
        if value < 0 or value >100:
            raise ValueError("score must between 0 and 100")
        self._score = value

s =Student()
s.score = 67
print(s.score)#67

#s.score = 999#ValueError: score must between 0 and 100


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 1990
print(s.age)#27

#s.age = 30#AttributeError: can't set attribute

"""
@property广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
"""




