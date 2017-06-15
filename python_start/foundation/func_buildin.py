print(abs(-9))#9
print(pow(10,2))#100 10^2
print(pow(10,2,13))#9 10^2%13
print(10**2%13)#9

print(max(1,2,4.3,9.02,5,6,5.1))#9.02
list = [1,2,4.3,9.02,5,6,5.1]
print(max(list))#9.02  参数iterable(可迭代)

print("============================")

print(int("111234"))
#print(int("111234q"))#ValueError: invalid literal for int() with base 10: '111234q'
#print(int("1.23e3"))#ValueError: invalid literal for int() with base 10: '1.23e3'
print(float("1.34333e3"))#1343.33
print(bool(""))#False
print(bool("0"))#False
print(bool(0))#False


print("============================")

"""
函数名其实就是指向一个函数对象的引用，
完全可以把函数名赋给一个变量，
相当于给这个函数起了一个“别名”
"""
a = abs
print(a(-9))#9


print(hex(254678))#0x3e2d6
print(bin(255))#0b11111111