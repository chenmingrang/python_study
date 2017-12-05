#集合set

#去重
l1 = ["c", 'b', 'd', 'a', 'd']
s1 = set(l1)
print(s1)


#集合运算
a = [1, 2, 3, 4, 5, 6]
b = [1, 8, 3, 9, 0, 6]
#交集
print(set(a) & set(b))#{1, 3, 6}
#并集
print(set(a) | set(b))#{0, 1, 2, 3, 4, 5, 6, 8, 9}
#差集
print(set(a) - set(b))#{2, 4, 5}
#对称差集
print(set(a) ^ set(b))#{0, 2, 4, 5, 8, 9}