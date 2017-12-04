#range

print("*="*20, "range", "*="*20)
r = range(10)
print(type(r))
print(type(list(r)))

l1 = [x+2 for x in range(5)]
print("type of l1 is : %s" % type(l1), "; l1 = ", l1)

g1 = (x+2 for x in range(5))
print("type of g1 is : %s" % type(g1), "; 1g = ", g1)


#map大数据分析
#map(匿名函数，可迭代对象)
print("*="*20, "map", "*="*20)
print(list(map(lambda x : x*x, [1, 2, 3])))
print(list(map(lambda x, y : x+y, [1, 2, 3], [4, 5, 6])))

def f1(x, y):
    return (x, y)

l1 = list(range(6))
l2 = ['SUN', "MON", "TUE", "WEN", "THUR", "FRI", "SAT"]
print(list(map(f1, l1, l2)))


#filter
print("*="*20, "filter", "*="*20)
print(list(filter(lambda x : x%2 , [1, 2, 3, 4])))
def f2(x):
    if x in [2, 3, 6, 7]:
        return True
    else:
        return False
print(list(filter(f2 , [1, 2, 3, 4, 7])))


#reduce
print("*="*20, "reduce", "*="*20)
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x+y, [1,2,3,4], 5))
print(reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd'))


#sort
print("*="*20, "sort", "*="*20)
a = [1, 4, -5, 6, 9, 2, 3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)