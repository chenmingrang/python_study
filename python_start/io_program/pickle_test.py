"""
我们把变量从内存中变成可存储或传输的过程称之为序列化.在Python中叫pickling,
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
"""

import pickle
d1 = dict(name='Micheal',age = 20,score=88)
"""
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
"""
print(pickle.dumps(d1))

f = open('dump.txt','wb')
pickle.dump(d1, f)
f.close()

"""
反序列化
可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
"""

print("*="*30)

f = open('dump.txt','rb')
d2 = pickle.load(f)
f.close()
print(type(d2),";d2=",d2)
print(id(d1),';',id(d2))#内存地址不一样，不是同一个对象


print("*="*30)

f = open('dump.txt','rb')
b = f.read()
print(b)
d3 = pickle.loads(b)
print(d3)


"""
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
"""