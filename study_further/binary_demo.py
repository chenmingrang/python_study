"""
正数的原码、反码、补码都一样
负数的原码为正数的原码高位变为1、反码高位为1其余为原码取反、补码为反码加1
1 的原码、反码、补码
  0000 0000 0000 0001
-1的原码
  1000 0000 0000 0001
  反码
  1111 1111 1111 1110
  补码
  1111 1111 1111 1111

1取反 ~1
  补码   0000 0000 0000 0001
  取反   1111 1111 1111 1110 减1
  反码   1111 1111 1111 1101 高位不变，其余取反
  原码   1000 0000 0000 0010 得-2



-1 + 1 补码相加
  0000 0000 0000 0001
 +1111 1111 1111 1111
 =0000 0000 0000 0000

原码 = 补码的符号位不变-->数据位取反-->尾+1
"""
a = 18
print(bin(a))#0b10010
print(0b10010)
print(oct(a))#0o22
print(0o22)
print(hex(a))#0x12
print(0x12)

c = int(0xff)
print(c)#255