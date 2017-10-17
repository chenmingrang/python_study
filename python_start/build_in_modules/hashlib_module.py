#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
"""
摘要算法又称哈希算法、散列算法:
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
"""


import hashlib
print('*='*10 ,'MD5', '*='*10)
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print('====多次update与一次的值一样====')
#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'Nobody inspects the spammish repetition')
print(m2.hexdigest()==m.hexdigest())#True
"""MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示"""

print('*='*10 ,'SHA1', '*='*10)
sha1 = hashlib.sha1()
sha1.update(b'how to use sha1 in Python.')
print(sha1.hexdigest())#b4be063c9e3461ddbd50dcbc345de18bb4b29205

sha2 = hashlib.sha1()
sha2.update(b'how to use sha1')
sha2.update(b' in Python.')
print(sha2.hexdigest()==sha1.hexdigest())#True
"""
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
有可能两个不同的数据通过某个摘要算法得到了相同的摘要，但是非常非常困难。
"""

"""
摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，
不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
"""