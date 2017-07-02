x=abs(-10)
print(x)#10

f=abs
print(f(-123))#123


#传入函数
def math(x, y, f):
    return f(x)+f(y)

print(math(1,-26,abs))#27
print(math(1,-26,f))#27

def func(x):
    return x**2;


#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
print(math(2,3,func))#13