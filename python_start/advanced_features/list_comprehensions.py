#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(range(1,11))
print(l1)

#[1x1, 2x2, 3x3, ..., 10x10]
l2 = []
for x in range(1,11):
    l2.append(x*x)
print(l2)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l3 = [x*x for x in range(1,11)]
print(l3)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l4 =[x*x for x in l1]
print(l4)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l5 = [x*x for x in l1 if x%2==0]
print(l5)#[4, 16, 36, 64, 100]

l6 = [m+n for m in "ABC" for n in "XYZ"]
print(l6)#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#显示当前目录下的文件
import os
files = [d for d in os.listdir("./")]
print(files)#['iteration.py', 'list_comprehensions.py', 'sub_object.py']


d={"a":1,"b":2,"c":3}
for k,v in d.items():
    print(k,'=',v)


l7 = [str(k)+'='+ str(v) for k,v in d.items()]
print(l7)#['b=2', 'a=1', 'c=3']


#将所有的小写转换为大写
l8 = ['a','b','c','d']
l8 = [x.upper() for x in l8]
print(l8)#['A', 'B', 'C', 'D']

l8=['hello','world',18,'age']
l8=[x for x in l8 if not isinstance(x,(int,float))]
print(l8)#['hello', 'world', 'age']

l8=[x.upper() for x in l8 if not isinstance(x,(int,float))]
print(l8)#['HELLO', 'WORLD', 'AGE']




