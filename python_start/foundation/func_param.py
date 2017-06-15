"""
   定义函数的时候，我们把参数的名字和位置确定下来，
函数的接口定义就完成了。
   对于函数的调用者来说，只需要知道如何传递正确的参数，
以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解
   Python的函数定义非常简单，但灵活度却非常大。
除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
"""

#位置参数(按参数的位置调用时传值)
def power(x):
    return x*x

print(power(-4))

def power(x,n):
    s = 1
    if not isinstance(n,(int)) or n<0:
        raise TypeError("n必须为0或正整数!")
    while n > 0:
        n=n-1
        s = s*x
    return s

print(power(-3, 3))#-27
#print(power(3))# power() missing 1 required positional argument: 'n'


#设置默认值(最大的好处是能降低调用函数的难度)
def power(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(power(-4))#16
print(power(3,3))#27


#example
def params(a,b,c="default c",d="default d"):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)
    print("=====================")

params("I'm a","I'm b")
params("I'm a","I'm b","I'm c")
params("I'm a","I'm b",d="I'm d")
params("I'm a","I'm b","I'm c","I'm d")


#==================默认参数陷阱==================
def add_to_list(l = []):
    l.append("END")
    return l

print(add_to_list([1,2,3]))#[1, 2, 3, 'END']
print(add_to_list(['a','b','c']))#['a', 'b', 'c', 'END']
#be careful
print(add_to_list())#['END']
print(add_to_list())#['END', 'END']
"""
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了
##########所以，定义默认参数要牢记一点：默认参数必须指向不变对象！##########
"""

def add_to_list(a=None):
    if a is None:
        a = []
    a.append("END")
    return a

print('===========================')
print(add_to_list())#['END']
print(add_to_list())#['END']
print(add_to_list(['x','y','z']))#['x', 'y', 'z', 'END']



#==================可变参数==================
"""
   在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，
可以是1个、2个到任意个，还可以是0个。
"""

def sum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print("=================================")
print(sum([1,2,3,4]))#30
print(sum((1,2,3,4)))#30
print(sum(set([1,2,3,4])))#30
print(sum({1:11,2:21,3:31,4:41}))#30


"""
   定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，
可以传入任意个参数，包括0个参数.
"""
def sum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print("=================================")
print(sum())#0
print(sum(1,2,3))#6
print(sum(1,2,3,4,))#10

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
list = [1,2,3,4,5,6]
print(sum(*list))#21



#==================关键字参数==================
"""
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
"""


def person(name,age,**kw):
    print("name=",name,"age=",age,"other=",kw)

person("Micheal",28)
#name= Micheal age= 28 other= {}

person("Micheal",28,CITY = "Beijing")
#name= Micheal age= 28 other= {'CITY': 'Beijing'}

person("Micheal",28,CITY = "Beijing")
#name= Micheal age= 28 other= {'CITY': 'Beijing'}

person("Micheal",28,CITY = "Beijing",job="manager")
#name= Micheal age= 28 other= {'CITY': 'Beijing', 'job': 'manager'}


#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
"""
****注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。****
"""
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("Micheal",28,**extra)
#name= Micheal age= 28 other= {'city': 'Beijing', 'job': 'Engineer'}



#==================命名关键字参数==================
def person(name,age,**kw):
    if "city" in kw:
        print(kw.get("city"))
    if "job" in kw:
        print(kw.get("job"))#Engineer
    print("name=",name,"age=",age,"other=",kw)

person('Jack', 24, job='Engineer',addr="zhengzhou")
#name= Jack age= 24 other= {'job': 'Engineer', 'addr': 'zhengzhou'}


#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。

def person(name,age,*,city,job):
    print("name=", name, "age=", age, "city=", city,"job=",job)


person("Micheal",30,city="Beijing",job="Manager")
#name= Micheal age= 30 city= Beijing job= Manager


#person("Micheal",30,city="Beijing")
# #TypeError: person() missing 1 required keyword-only argument: 'job'


def person(name,age,*,city="Shanghai",job):
    print("name=", name, "age=", age, "city=", city, "job=", job)


person("Micheal",30,job="Engineer")
#name= Micheal age= 30 city= Shanghai job= Engineer

"""
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
"""


#==================参数组合==================
"""
   在Python中定义函数，可以用
***必选参数、默认参数、可变参数、关键字参数和命名关键字参数***，
这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
***必选参数、默认参数、可变参数、命名关键字参数和关键字参数***。
"""

def func1(a, b, c=0, *args, **kw):
    print("a=",a,"b=",b,"c=",c,"args=",args,'kw=',kw)

def func2(a,b,c=0,*,d,**kw):
    print("a=", a, "b=", b, "c=", c,"d=",d,'kw=', kw)

func1(1,2)#a= 1 b= 2 c= 0 args= () kw= {}
func1(1,2,3)#a= 1 b= 2 c= 3 args= () kw= {}
func1(1,2,3,'a','b')#a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
func1(1,2,'a','b',y=90)#a= 1 b= 2 c= a args= ('b',) kw= {'y': 90}
func1(1,2,3,'a','b',x=99)#a= 1 b= 2 c= 3 args= ('a', 'b') kw= {'x': 99}

#d为关键字
func2(1,2,33,d=44)#a= 1 b= 2 c= 33 d= 44 kw= {}
func2(1,2,d=44,key="value")#a= 1 b= 2 c= 0 d= 44 kw= {'key': 'value'}

print("===================================")
args = (1,2,3,4,22)#前三个赋给位置参数，后面的元素赋给可变参数
kw = {"ab":99,"ac":"val_ac"}
func1(*args,**kw)#a= 1 b= 2 c= 3 args= (4, 22) kw= {'ab': 99, 'ac': 'val_ac'}

args = (3,5,6)#必须三个元素
kw = {"d":"val_abc","def":"val_def"}#必须含有d关键字
func2(*args,**kw)#a= 3 b= 5 c= 6 d= val_abc kw= {'def': 'val_def'}



def func3(a,b,*c,d):
    print("a=",a,"b=",b,"c=",c,"d=",d)

func3(1,2,d=9)#a= 1 b= 2 c= () d= 9
c = [2,3,5,8,89,66]
func3(*(1,2,3,4,5),d=99)#a= 1 b= 2 c= (3, 4, 5) d= 99
func3(*c, d="keyb")#a= 2 b= 3 c= (5, 8, 89, 66) d= keyb

print("==========================")

def func4(a, b, *, key=9):
    print(a,b,"key=",key)

#print(func4(1, 4, 33))#TypeError: func4() takes 2 positional arguments but 3 were given
print(func4(2, 4, key=8888))#2 4 key= 8888
print("==========================")

"""
******************************************************************
****所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，****
****无论它的参数是如何定义的。                                    ****
******************************************************************
"""


