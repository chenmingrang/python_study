names=["Jack","Rose","Tom","Green"]
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum = sum + x
print(sum)

list = list(range(101))
print(list)
sum=0
for x in list:
    sum = sum + x
print(sum)


sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


n = 100
while n > 0:
    if n==10 or  (n/2)==27 :
        print(n)
        break
    n = n -1

n = 21
sum = 0
while n > 0:
    n = n - 1
    if (n%2)==1:
        continue
    else:
        print(n)
        sum = sum + n

print(sum)

