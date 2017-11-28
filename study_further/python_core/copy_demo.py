#深拷贝和浅拷贝

#浅拷贝（同一个引用）
a = [11, 22, 33]
b = a
print(id(a))
print(id(b))


#深拷贝
print("*="*15, '深拷贝', "*="*15)
import copy
c = copy.deepcopy(a)
print(id(a))
print(id(c))
print(a==c)

print('a.append(44)')
a.append(44)
print('a=', a)
print('b=', b)
print('c=', c)
