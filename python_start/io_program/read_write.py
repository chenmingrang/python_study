
f = open('d:/ttt.txt','r')
for item in f:
    print(item,end='')

#如果文件不存在，open()函数就会抛出一个IOError的错误
#f1 = open('d:/wwww.txt')#FileNotFoundError

print("*#"*30)

f2 = open('d:/ttt.txt','r')
print(f2.read())
f2.close()


try:
    f = open('d:/22.txt','r')
    print(f.read())
except FileNotFoundError as e:
    print(e.strerror)#No such file or directory
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法

print("*#"*30)

try:
    with open('d:/ttt.txt1','r') as f:
        print(f.readline())
except Exception as e:
    print(e)

#二进制文件
f = open(r'D:\apache-tomcat-7.0.54\webapps\docs\images\tomcat.gif','rb')
print(f.read())

#字符编码
f = open(r"d:\testGbk.txt",'r',encoding='gbk')
print(f.read())

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符.
#遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略

f = open(r"d:\testGbk.txt",'r',encoding='gbk',errors="ignore")
print(f.readline())

#写文件
import os
os.remove(r'd:\testWrite.txt')
with open(r"d:\testWrite.txt",'a',encoding='gbk') as f:
     f.write("测试")

with open(r"d:\testWrite.txt", 'a', encoding='utf-8') as f:
    f.write("测试")

f = open(r"d:\testWrite.txt",'r')
print(f.readline())
f = open(r"d:\testWrite.txt",'r',encoding='gbk',errors="ignore")
print(f.readline())
f.close()#释放资源