import re

#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
#str1 = '010-33332322'#ok
#str1 = '010-33332322'#ok
#str1 = '010 33332322'#ok
str1 = '0371 33332322'#ok
if re.match(r'^\d{3,4}(-?|\s*)\d{7,8}',str1):
    print('ok')
else:
    print('failed')


print("=============字符串切割=============")
print("22  000 00".split(' '))
print(re.split(r'\s+', '22  000 00'))
print(re.split(r'[\s\,\;]+', 'a,b;c  d, e;   f'))

print("=============分组=============")
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
str2 = '0371-84735555aaad'
m  = re.match(r'^(\d{3,4})(-?|\s*)(\d{7,8})', str2)
print(m.group(0))#group(0)永远是原始字符串
print(m.group(1))#group(1)表示第一个子串
print(m.group(2))
print(m.group(3))
print(m.group(1)+" "+m.group(3))

