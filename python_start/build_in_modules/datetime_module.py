#datetime是Python处理日期和时间的标准库
#encoding=utf-8

"""
注意到datetime是模块，datetime模块还包含一个datetime类，
通过from datetime import datetime导入的才是datetime这个类
"""

from datetime import datetime
now = datetime.now()
print(now)
print(type(now))#<class 'datetime.datetime'>

dt = datetime(2017, 10 , 1, 12 ,10)
print(dt)#2017-10-01 12:10:00
print(dt.time())#12:10:00
print(dt.date())#2017-10-01
#从星期1开始算起（0）
print(datetime(2017, 10, 15).weekday())#6


print("*="*30)
#datetime转换为timestamp
"""
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
timestamp的值与时区毫无关系
类似：
timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
"""

#最后一位是微秒
dt = datetime(2012, 6, 20, 13, 40, 40, 8)
#Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
print(dt.timestamp())#1340170840.000008


#timestamp转换为datetime
print("*="*30)

t = 0.8
#默认时区是东8区
#本地时间
print(datetime.fromtimestamp(t))#1970-01-01 08:00:00.800000
#UTC时间
print(datetime.utcfromtimestamp(t))#1970-01-01 00:00:00.800000


print("*="*30)
#str转化为datetime
cday = datetime.strptime('2016-11-23 13:59:00', '%Y-%m-%d %H:%M:%S')
print(cday)#2016-11-23 13:59:00

now = datetime.now()
date_str = now.strftime(r'%b %d %Y %H:%M:%S')
print(date_str)
print(now.strftime('%A'))