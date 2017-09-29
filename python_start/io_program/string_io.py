'''
    StringIO顾名思义就是在内存中读写str
    很多时候，数据读写不一定是文件，也可以在内存中读写
'''
from io import StringIO
f = StringIO()
len = f.write('hello')
print(len)#5
len = f.write(" ")
print(len)#1
len = f.write("world!")
print(len)#6
print(f.getvalue())#hello world!

print("#*"*30)

f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())

print("#*"*30)
#ByteIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
len = f.write('中文'.encode('utf-8'))
print(len)#6
len = f.write('中文'.encode('gbk'))
print(len)#4
print(f.getvalue())

f = BytesIO(b"\xd6\xd0\xce\xc4")
print(str(f.read(),encoding='gbk'))#中文



