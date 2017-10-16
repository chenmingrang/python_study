#Base64是一种用64个字符来表示任意二进制数据的方法
#Base64是一种最常见的二进制编码方法
"""
Base64的原理很简单，首先，准备一个包含64个字符的数组：
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit(对应十进制是0-63)
这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
2进制： 01110011 00110001 00110011
6个一组（4组） 011100 110011 000100 110011
高位补0  00011100 00110011 00000100 00110011
得到 28 51 4 51
查对下照表 c z E z
"""

import base64
en_str = base64.b64encode(b'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.')
print(en_str)
print(base64.b64decode(en_str))

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))#b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))#b'abcd--__'
print(base64.urlsafe_b64decode(b'abcd--__'))#b'i\xb7\x1d\xfb\xef\xff'

print(base64.b64encode('在Python中使用base64编码'.encode('utf-8')))
print(base64.urlsafe_b64encode('在Python中使用base64编码'.encode('utf-8')))

#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
def safe_base64_decode(de_str):
    if(len(de_str) % 4 == 3):
        de_str = de_str + '='
    elif(len(de_str) % 4 == 2):
        de_str = de_str + '=='
    print('-----', de_str)
    return base64.b64decode(de_str)



def safe_base64_encode(en_str):
    en_bytes = base64.b64encode(en_str.encode('utf-8'))
    return str(en_bytes).replace("=", "")

print(safe_base64_encode('abcd'))#b'YWJjZA'
print(safe_base64_decode('YWJjZA'))#b'abcd'