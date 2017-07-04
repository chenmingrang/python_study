#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

L=list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9]))
print(L)#[1, 4, 9, 16, 25, 36, 49, 64, 81]

def f1(x):
    return x**2

L= list(map(f1,[1,2,3,4,5,6,7,8,9]))
print(L)#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f = lambda x : x**2
print(f)#<function <lambda> at 0x000002DCEE2F50D0>
print(f(5))#25

def build(x, y):
    return lambda: x**2 + y**2

print(build(2,3))#<function build.<locals>.<lambda> at 0x0000020F0CA751E0>
print(build(2,3)())#13