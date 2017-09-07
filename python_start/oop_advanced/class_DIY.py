#Python的class中有许多特殊用途的函数，可以帮助我们定制类

#__init__
class Student():
    def __init__(self,name):
        self.name = name

s = Student("Micheal")
print(s.name)#Micheal
print(s)#<__main__.Student object at 0x0000019D91D7DD30>

#__str__
class Student():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Student object (name: %s)" % self.name

s = Student("Micheal")
print(s)#Student object (name: Micheal)


#__iter__
"""
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环
"""

class Fib():
    def __init__(self):
        self.a ,self.b =0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a ,self.b = self.b , self.a + self.b
        if self.a >1000:
            raise StopIteration()
        return str(self.a) + " " +str(self.b)

for i in Fib():
    print(i)

#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素

fib = Fib()
#print(fib()[5])#TypeError: 'Fib' object is not callable


#__getitem__

class Fib():
    def __getitem__(self, item):
        a , b = 1 , 1
        for x in range(item):
            a , b = b , a+b
        return str(a) + " " + str(b)

fib = Fib()
print(fib[5])#8 13

print(fib[50])#20365011074 32951280099



print("==========切片===========")
#但是list有个神奇的切片方法：
print(list(range(1,10))[::2])#[1, 3, 5, 7, 9]


class Fib():
    def __getitem__(self, n):
        if isinstance(n,int):
            a ,b =1, 1
            for x in range(n):
                a ,b = b ,a+b
            return a
        if isinstance(n, slice):
            start = n.start if  n.start is not None else 0
            stop = n.stop
            print(start)
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])#[1, 1, 2, 3, 5]
print(f[:10])#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


print("==========__getattr__===========")

class Student(object):

    def __init__(self):
        self.name = "Micheal"

s = Student()
print(s.name)#Micheal
#print(s.score)#AttributeError: 'Student' object has no attribute 'score'


class Student(object):

    def __init__(self):
        self.name = "Michael"


    def __getattr__(self, item):
        if item == 'score':
            return 99

s = Student()
print("........")
print(s.name)#Michael
print(s.score)#99

#返回函数也是可以的

class Student():

    def __getattr__(self, item):
        if item == 'age':
            return lambda :28

s = Student()
print(s.age())#28
print(s.addr)#None

#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
#注意到任意调用如s.addr都会返回None，这是因为我们定义的__getattr__默认返回就是None


class Student():

    def __getattr__(self, item):
        if item == 'age':
            return lambda :28
        raise AttributeError('"Student" object has no attribute "%s"' % item)

s = Student()
#print(s.addr)#AttributeError: "Student" object has no attribute "addr"

print("===============chain===============")
#利用完全动态的__getattr__，我们可以写出一个链式调用

class Chain():
     def __init__(self, path=''):
         self._path = path

     def __getattr__(self, path):
         return Chain("%s/%s" % (self._path, path))

     def __str__(self):
         return self._path

     __repr__ = __str__

print(Chain().status.user.timeline.list)#/status/user/timeline/list


class Chain():
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __call__(self,name):
        return Chain(self._path + "/"+ name)

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().eee.users("micheal").repos)#/eee/users/micheal/repos
print(Chain().ww.ee.users("Stiff").repos)#/ww/ee/users/Stiff/repos


#__call__

class Student():
    def __init__(self,name):
        self.name =name

    def __call__(self):
        print("My name is %s." % self.name)


s1 = Student("Jack")
s1()#My name is Jack.
"""
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
"""

##我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print("===================")
print(callable(Student))#True
print(callable(max))#True
print(callable(None))#False
print(callable([1,2,3]))#False
print(callable("str"))#False

