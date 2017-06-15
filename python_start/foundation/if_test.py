age=20
print("your age is ",age)
if age >=18:
    print("adult")

age=3
print("your age is ",age)
if age >=18:
    print("adult")
else:
    print("teenager")

age=12
print("your age is ",age)
if age>=18:
    print("adult")
elif age>=6:
    print("teenager")
else:
    print("kid")


#只要x是非零数值、非空字符串、非空list等，
# 就判断为True，否则为False。
x=""
x=[]
x=0
if x:
    print(True)
else:
    print(False)


#year=int(input("enter your birth\n"))
year=2016
if year>2000:
    print("00后")
else:
    print("00前")



bmi=80.5/pow(1.72,2)
print("%.2f" % bmi)
if bmi>=32:
    print('严重肥胖')
elif bmi>=28:
    print('肥胖')
elif bmi>=25:
    print("过重")
elif bmi>=18.5:
    print("正常")
else:
    print("过轻")







