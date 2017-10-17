#准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。

#python中把一个32位整数变成字节，也就是4个长度的bytes
print('*='*10, '整数-->数组', '*='*10)
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)


print('*='*10, 'struct的pack函数把任意数据类型变成bytes', '*='*10)

import struct
print(struct.pack('>IH', 10240099, 9992))#b"\x00\x9c@c'\x08"
print(struct.pack('>I', 10240099))#b'\x00\x9c@c'
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print(struct.unpack('>IH',  b'\xf0\xf0\xf0\xf0\x80\x80'))
"""
尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了
"""


