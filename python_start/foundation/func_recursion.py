#计算阶乘n! = 1 x 2 x 3 x ... x n
def recur(n):
    if n == 1:
        return 1
    else:
        return n*recur(n-1)

print(recur(5))#120


#使用递归函数需要注意防止栈溢出。
#print(recur(1000))#RecursionError: maximum recursion depth exceeded in comparison

"""
  解决递归调用栈溢出的方法是通过尾递归优化，
  事实上尾递归和循环的效果是一样的，
  所以，把循环看成是一种特殊的尾递归函数也是可以的。
"""


def fact(n):
    return fact_iter(n,1)

def fact_iter(num,result):
    if num==1:
        return result
    return fact_iter(num-1,num*result)

print(fact(5))#120
"""
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120

   尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

   遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
"""


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


list = []
n = 1
while n<=99:
    list.append(n)
    n = n+2
print(list)







