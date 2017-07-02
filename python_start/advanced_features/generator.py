"""
   如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()
L = [x * x for x in range(10)]
print(L)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(5))
print(g)  # <generator object <genexpr> at 0x0000023B2685B4C0>

# 打印generator的每一个元素
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
print(next(g))  # 9
print(next(g))  # 16
# print(next(g))#StopIteration

# for循环迭代generator对象(不需要关心StopIteration的错误)
for n in g:
    print(n)

print("=====================================")


# 斐波那契额函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        t = a
        a = b
        b = a + t
        # a,b=b,a+b#与上面的写法效果一样
        n = n + 1
    return "done"


fib(6)


print("===========generator实现斐波那契额函数===========")
# generator实现斐波那契额函数
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"

f = fib2(6)
print(f)#<generator object fib at 0x0000021B1701B5C8>
for n in f:
    print(n)
print("===========generator实现斐波那契额函数===========")


f = fib2(6)
while True:
    try:
        x = next(f)
        print("f:",x)
    except StopIteration as e:
        print("generator return value:",e.value)
        break
#最后输出“generator return value: done”

print("=========================================")
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3
    print("step 3")
    yield 5

o = odd()
print(o)#<generator object odd at 0x000001AE4289B5C8>
for i in o:
    print(i)


print("====杨辉三角====")
#杨辉三角
def triangles(n):
    L=[1]
    i=1
    while i<n:
        yield L
        L=[0]+L+[0]
        L=[L[s]+L[s+1] for s in range(i+1)]
        i+=1

tri=triangles(10)
for i in tri:
    print(i)


