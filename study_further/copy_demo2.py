print("*="*15, '深拷贝1', "*="*15)
m = [11, 22, 33]
n = [44, 55, 66]
p = [m, n]
q = p
print(q is p)#True

import copy
r = copy.deepcopy(p)#深拷贝（递归拷贝）
print(r == p)#True
print(r is p)#False

m.insert(0, 00)
print(p)#[[0, 11, 22, 33], [44, 55, 66]]
print(q)#[[0, 11, 22, 33], [44, 55, 66]]
print(r)#[[11, 22, 33], [44, 55, 66]]

print("*="*15, '深拷贝2', "*="*15)

a = [11, 22, 33]
b = [44, 55, 66]
c = [a, b]
e = copy.copy(c)#只拷贝第一层，后面层次为同一引用
a.append(44)
print(c[0])
print(e[0])
print(c[0] is e[0])#True

print("*="*15, '深拷贝3（tuple1）', "*="*15)
x = [11, 22, 33]
y = [44, 55, 66]
w = (x, y)
z = copy.deepcopy(w)
x.append(44)
print(w)#([11, 22, 33, 44], [44, 55, 66])
print(z)#([11, 22, 33], [44, 55, 66])
print(w is z)#False


print("*="*15, '深拷贝4（tuple2）', "*="*15)
x = [11, 22, 33]
y = [44, 55, 66]
w = (x, y)
z = copy.copy(w)#元组是不可变类型
x.append(44)
print(w)#([11, 22, 33, 44], [44, 55, 66])
print(z)#([11, 22, 33, 44], [44, 55, 66])
print(w is z)#True