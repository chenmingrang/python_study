from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dev'))

for name,member in Month.__members__.items():
    print("name : %s; member:%s" % (name,member))


from enum import unique

#@unique装饰器可以帮助我们检查保证没有重复值

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)#Weekday.Mon
print(Weekday.Thu)#Weekday.Thu
print(Weekday['Sat'])#Weekday.Sat
print(Weekday.Wed.value)#3
print(Weekday(1))#Weekday.Mon
#print(Weekday(7))#ValueError: 7 is not a valid Weekday
print(Weekday(1)==Weekday.Mon)#True

for name,member in Weekday.__members__.items():
    print('%s==>%s,value=%s' % (name,member,member.value))


#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。


