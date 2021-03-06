#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1,2,3,4,5,6))#21


def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6)
print(f)#<function lazy_sum.<locals>.sum at 0x00000216529D5268>

print(f())#21


"""
    在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。
"""

"""当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数"""
#f1()和f2()的调用结果互不影响
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1==f2)#False



#返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

"""
全部都是9！原因就在于返回的函数引用了变量i，
但它并非立刻执行。等到3个函数都返回时，
它们所引用的变量i已经变成了3，因此最终结果为9
"""

L = count()
print(L[0]())#9
print(L[1]())#9
print(L[2]())#9
#返回函数不要引用任何循环变量，或者后续会发生变化的变量


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
    return fs

L=count()
print(L[0]())#1
print(L[1]())#4
print(L[2]())#9