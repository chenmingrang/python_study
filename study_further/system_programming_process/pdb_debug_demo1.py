#pdb 断点调试 python -m pdb pdb_debug_demo1.py
#l-->list 显示当前的代码
#n-->next 向下执行的代码
#c-->continue 继续执行代码(遇到断点停止)
#b num-->break 添加断点
#clear-->删除断点
#p-->打印一个变量的值
#a-->打印所有的形式参数
#s-->step进入到一个函数
#q-->退出调试
def avg(a, b):
    result = a + b
    return result//2

a = 100
b = 200
c = a + b
ret = avg(a, b)
print(ret)