####################### type类型判断  #######################
print(type(123))#<class 'int'>
print(type('2223'))#<class 'str'>
print(type(None))#<class 'NoneType'>
print(type(abs))#<class 'builtin_function_or_method'>

def add(x,y):
    return x+y

print(type(add))#<class 'function'>

class Animal():
    def run(self):
        print("Animal is running!")

print(type(Animal))#<class 'type'>

a = Animal()
print(type(a))#<class '__main__.Animal'>

print(type(178)==type(234))#True
print(type("abc") == type(123))#False

import types
def f(n):
    pass

#自定义函数
print(type(f) == types.FunctionType)#True
#内置函数
print(type(abs)==types.BuiltinFunctionType)#True
#lambda表达式
print(type(lambda x:x) == types.LambdaType)#True
#生成器类型
print(type(x for x in range(1,10))==types.GeneratorType)#True
print("=========================================")

####################### isinstance对象类型  #######################

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()
print(isinstance(a,object))#True
print(isinstance(d,Animal))#True
print(isinstance(h,Animal))#True
print(isinstance(h,Dog))#True

print(isinstance(a,Dog))#False

#能用type()判断的基本类型也可以用isinstance()判断
print("=========================================")
print(isinstance('a',str))#True
print(isinstance(123,int))#True
print(isinstance(b'2',bytes))#True
print(isinstance(lambda x : x,types.LambdaType))#True


#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print("=========================================")
print(isinstance([1,'str'],(list,tuple)))#True
print(isinstance((1,'str'),(list,tuple)))#True



####################### dir获得一个对象的所有属性和方法  #######################
print(dir("ABC"))#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法
'''
print(len("abc"))#3
print("abc".__len__())#3

class MyObj(object):
    def __len__(self):
        return 10

o = MyObj()
print(len(o))#10
print(o.__len__())#10

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
print('=========================================')

class MyObject(object):
    def __init__(self):
        self.x = 8
    def power(self):
        return self.x**2

obj = MyObject()
print(hasattr(obj,'x'))#True
print(obj.x)#8
print(hasattr(obj,'y'))#False
setattr(obj,'y',10)
print(hasattr(obj,'y'))#True
print(getattr(obj,'y'))#10
print(obj.y)#10
setattr(obj,'x',100)
print(obj.power())#10000

print('==================================')
#print(getattr(obj,'w'))#AttributeError: 'MyObject' object has no attribute 'w'
setattr(obj,'w',900)
print(getattr(obj,'w'))#900

print(hasattr(obj,'power'))#True
fn = getattr(obj,'power')
print(fn)#<bound method MyObject.power of <__main__.MyObject object at 0x000001DB889564A8>>
print(fn())#10000

















