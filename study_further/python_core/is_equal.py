#==判断值是否相等，is判断是否指向同一个对象

a = [11, 22, 33]
b = [11, 22, 33]

print(a==b)#True

print(id(a))
print(id(b))
print(a is b)#False

c = a
print(b == c)#True
print(a is c)#True

print("==========================")
#常量池
d = 100
e = 100
print(d == e)#True
print(e is d)#True