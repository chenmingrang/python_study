"""
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令;
其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数;
Python内置的os模块可以直接调用操作系统提供的接口函数
"""
import os
print(os.name)

#os模块的某些函数是跟操作系统相关的。
#print(os.uname())linux系统提供的命令

"""环境变量"""
print(os.environ)

"""获取摸个环境变量"""
print(os.environ.get("JAVA_HOME"))#C:\Program Files (x86)\Java\jdk1.8.0_121
print(os.environ.get("x","default"))


"""操作文件与目录"""
"""
   把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
   这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串;
   同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()
"""
#查看当前目录
print(os.path.abspath("."))#D:\python_study\python_start\io_program
#在某个目录下创建新的目录，首先把新目录的完整路径表示出来
print(os.path.join('D:\\','test'))#D:\test
os.mkdir(r'D:\test')
os.rmdir(r'D:\test')
print(os.path.split(r'D:/python_study/python_start/foundation/dict_and_set.py'))
"""这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。"""
try:
    os.remove("d:/test11.txt")
except Exception as e:
    print(e)

try:
    os.remove("d:/test11.py")
except Exception as e:
    print(e)

f = open("d:/test11.txt", 'a')
f.close()
os.rename("d:/test11.txt","d:/test11.py")

#shutil模块是对os模块的补充
import shutil
shutil.copyfile("d:/test11.py","d:/test11_copy.py")

print("*="*30)
l = [x for x in os.listdir('.')]
print(l)
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)