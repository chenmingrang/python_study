"""
定义函数关键字:def
    如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
    return None可以简写为return
"""
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-9))#9

def none_fun():
    return

print(none_fun())#None


#pass(与pl/sql中的null功能一致)
"""
实际上pass可以用来作为占位符，
比如现在还没想好怎么写函数的代码，
就可以先放一个pass，让代码能运行起来。
"""
def nothing():
    pass

print(nothing())


def changeVal(x):
    if x>=10:
        x = x*3
    elif x>5:
        x = x*2
    else:
        pass
    return x

x = 8
y = 3
print(changeVal(x))#16
print(changeVal(y))#3


"""
参数检查
   自定的my_abs无参数检查，而内置函数abs则有参数检查
"""
#print(my_abs("aaa"))#TypeError: unorderable types: str() >= int()
#print(abs("es"))#TypeError: bad operand type for abs(): 'str'


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-1.4567))#1.4567
print(my_abs(-13))#13
#print(my_abs("1"))#TypeError: bad operand type



"""
返回多个值
   返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
   而多个变量可以同时接收一个tuple，按位置赋给对应的值，
   所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
"""

import math
def movement(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

x,y = movement(100,100,60,math.pi/6)
print(x,y)#151.96152422706632 130.0
x = movement(100,100,60,math.pi/6)
print(x)#(151.96152422706632, 130.0)
print(len(x))#2


"""
    1、定义函数时，需要确定函数名和参数个数；
    2、如果有必要，可以先对参数的数据类型做检查；
    3、函数体内部可以用return随时返回函数结果；
    4、函数执行完毕也没有return语句时，自动return None。
    5、函数可以同时返回多个值，但其实就是一个tuple。
"""

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
def formula(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)

print(formula(1,4,4))#(-2.0, -2.0)
print(formula(2,3,1))#(-0.5, -1.0)