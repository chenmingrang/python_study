# 对应的ascii码值
print(ord('A'))
print(ord('中'))
# 放回ascii码值或Unicode对应的字符
print(chr(66))
print(chr(25991))
x = b'ABC'
print(len(x))
print('\u4e2d\u6587')
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b"ABC"))  # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6
print(len("中文"))  # 2
print(len("中文".encode("GBK")))  # 4 一个汉字2个字节
print(len("中文".encode("utf-8")))  # 6一个汉字3个字节

# 格式化（%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略）
# %s 字符串  %x 十六进制整数  %d  整数  %f  浮点数
print("hello %s!How old are you? \nI'm %d" % ("JIm", 29.22))  # 显示29
print("hello %s!How old are you? \nI'm %f" % ("JIm", 29.22))  # 显示29.220000

print("%2d-%02d" % (2, 3))  # " 2-03"
print("%02d-%02d" % (12, 3))  # "12-03"
print("%02d-%02d" % (112, 333))  # "112-333"
print("%.2d-%02d" % (2, 28))  # "02-28"

print("%.2f" % 3.14523)  # "3.15"
print("%.3f" % 3.14523)  # "3.145"

# 增加比例
print('%.2f%%' % ((85 - 72) / 72 * 100))  # 18.06%
