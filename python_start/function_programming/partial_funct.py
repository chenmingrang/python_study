#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。

print(int('19'))#123345
print(int('7777',base=8))#4095
print(int('EEEE',16))#61166
print(int('11111111',2))#255


"""
functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单
"""
import functools
int2 = functools.partial(int,base=2)
print(int2('1111'))#15

#在函数调用时传入其他值
print(int2('eeee',base=16))#61166









