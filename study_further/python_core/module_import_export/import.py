import sys

#从前往后查找，找到之后不再查询接下的模块
print(sys.path)

#导入模块增加D:\books路径
sys.path.append("D:\\books")
print(sys.path)

#重新导入模块

from imp import *
#重新加载模块
#reload("D:\\books")#argument must be module
