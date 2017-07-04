#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小

print(sorted([36,-9,13,45,2]))#[-9, 2, 13, 36, 45]

#可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36,-9,13,45,2],key=abs))#[2, -9, 13, 36, 45]

#默认情况下，对字符串排序，是按照ASCII的大小比较的
#['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#忽略大小写
#['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))

#反向排序
#['Zoo', 'Credit', 'bob', 'about']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))
#[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
print(sorted(L,key=lambda item:item[1]))
#[('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]


m={1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(m))#[1, 2, 3, 4, 5]
