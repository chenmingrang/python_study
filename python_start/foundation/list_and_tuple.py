#==================python内置的list与js的数组类似==================#
classmates = ['Jim','Green','Tom']
print(classmates)
print(len(classmates))
print(classmates[1])
#print(classmates[3])#list index out of range

#取最后一个元素
print(classmates[-1])

classmates.append('Lucy')#追加
classmates.insert(1,'Jack')
print(classmates)#['Jim', 'Jack', 'Green', 'Tom', 'Lucy']

#删除最后一个元素
classmates.pop()
print(classmates)#['Jim', 'Jack', 'Green', 'Tom']

classmates.pop(1)#删除Jack
print(classmates)#['Jim', 'Green', 'Tom']

#Green--->Micheal
classmates[1]="Micheal"
print(classmates)#['Jim', 'Micheal', 'Tom']

arr2=['java','c','c++',['python','javaScript']]
print(len(arr2))
print(arr2[3][1])#javaScript


#==================tuple与list类似，但是tuple一旦初始化就不能修改==================#
print('==========tuple==========')

classmates=('Micheal','Bob','Tracy')
print(classmates)
print(classmates[1])
print(classmates[-1])


#定义一个空的tuple
t=()
print(t)
print(len(t))

#当tuple只有一个元素时,不加“,”表示字符串或数字，而不是tuple
t1=(33)#表示数字，"()"为数学计算符
print(t1)
#print(len(t1))#运行报错

t2=("1")
print(t2)
print(len(t2))

t3=(1,)#(1,)tuple只有个一个元素时正确的表示
print(t3)
print(len(t3))

#=============tuple的可变性==============
t=("a","b",["A","B"])
print(t)#('a', 'b', ['A', 'B'])
t[2][0]="C"
t[2][1]="D"
print(t)#('a', 'b', ['C', 'D'])

#效果同上
list=["A","B"]
t=("a","b",list)
print(t)#('a', 'b', ['A', 'B'])
list[0]="C"
list[1]="D"
print(t)#('a', 'b', ['C', 'D'])


#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！












