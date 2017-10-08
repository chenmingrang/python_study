"""
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应:
    JSON类型	     Python类型
    {}	         dict
    []	         list
    "string"	 str
    1234.56	     int或float
    true/false	 True/False
    null	     None
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
"""
import json
d1 = dict(name='Micheal',age=20, score=99)
str1 = json.dumps(d1)
print(str1)

print("*="*30)

str2 = r'{"score": 95, "name": "Micheal", "age": 27}'
d2 = json.loads(str2)
print(type(d2),'; d2 = ',d2)


print("*="*30)
"""
Python的dict对象可以直接序列化为JSON的{}，
不过，很多时候，我们更喜欢用class表示对象，比如定义Student类
"""

class Student(object):
    def get_info(self):
        return "name = %s age = %d score = %d" % (self.name,self.age,self.score)
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Micheal',27,97)
print(s.get_info())
print(s.__dict__)
#print(json.dumps(s))#TypeError: <__main__.Student object at 0x00000170E917B4E0> is not JSON serializable
#编写一个转化函数
def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }

print(json.dumps(s,default=student2dict))#{"age": 27, "name": "Micheal", "score": 97}

#不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
print(json.dumps(s, default=lambda obj : obj.__dict__))#{"name": "Micheal", "age": 27, "score": 97}
"""
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
也有少数例外，比如定义了__slots__的class
"""


print("*="*30)
"""
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象,
然后，我们传入的object_hook函数负责把dict转换为Student实例
"""
str2 = r'{"age": 27, "score": 97, "name": "Micheal"}'

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(str2,object_hook=dict2student))#<__main__.Student object at 0x000001B8CAB0C8D0>


"""
Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
json模块的dumps()和loads()函数是定义得非常好的接口的典范。
当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性
"""


