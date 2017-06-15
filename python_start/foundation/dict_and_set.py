#dict的支持，dict全称dictionary，在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。
scores={"Micheal":98,"Green":96,"Tom":92}
name="Micheal"
print(scores[name])#98
scores["Jim"]=59.99
print(scores["Jim"])#59.99
#print(scores["JIM"])抛出异常

scores[name]=100
print(scores[name])#100

#需要牢记dict的key必须是不可变对象（字符串、数字等。list则不可以）
#判断是否存在
if "JIM" in scores:
    print(scores["JIM"])
else:
    print("there is not have a JIM")


#get(key),不存在返回none
#get(key,val),不存在返回val
print(scores.get("Jim"))
print(scores.get("JIM"))

print(scores.get("Jim",100))
print(scores.get("JIM","have no JIM"))


#pop删除一个key,操作之前先做下判断
scores.pop("Jim")
print(scores.get("Jim",-1))
#scores.pop("Tomson")#KeyError: 'Tomson'
print(scores.get("Tomson",-1))


#set也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。
#set的可以与dict的key一样必须是不可变对象（字符串、数字等。list则不可以）


set1 = set([1,2,3,45,1,2])#自动去重
print(set1)#{1, 2, 3, 45}
set1.add(34)
print(set1)#{1, 2, 3, 34, 45}
set1.remove(1)
set1.add(34)#不会重复添加
print(set1)#{2, 3, 34, 45}
#set1.remove(1)#KeyError: 1

#set2 = set(["11",["121","122"],11])#TypeError: unhashable type: 'list'
set2 = set(["11","22","s1",11])
print(set2)
set2.remove("11")#{11, 's1', '22'}
print(set2)


#集合运算 & |
s1 = set(["s1","s2","s3"])
s2 = set(["s3","s2","s4","s5"])
s = s1 & s2
print(s)#{'s3', 's2'}
s = s1 | s2
print(s)#{'s3', 's5', 's2', 's4', 's1'}
s = s1 -s2
print(s)#{'s1'}
s = s2 - s1
print(s)#{'s4', 's5'}

s = set([1,2,34,5])
t = tuple([1,2,3,4])#tuple不可变(引用不可变)
s.add(t)
print(s)#{1, 2, 34, 5, (1, 2, 3, 4)}


s = set([1,2,4])
#t = tuple([1,2,3,[1,2,3]])#TypeError: unhashable type: 'list'
t = tuple(["wwww",22])
s.add(t)
print(s)#{('wwww', 22), 1, 2, 4}


