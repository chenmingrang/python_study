def fib(num):
    print("======strat=======")
    a, b = 0, 1
    for i in range(num):
        print("======1=======")
        yield b#调用一次，遇到yield程序会停止，返回b
        print("======2=======")
        a, b = b, a+b
    print("======stop=======")


for i in fib(10):
    print(i)

print("*="*40)
ret = fib(6)
print(ret.__next__())

print("*="*20, "send test1", "*="*20)
def test():
    i = 0
    while i<5:
        temp = yield i
        print("temp =", temp)
        i += 1

t = test()
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
#send方法会把值赋给temp，也会让生成器往前执行
t.send("hello world")


print("*="*20, "send test2", "*="*20)
def test2():
    i = 0
    while i < 5:
        temp = yield i
        print("temp =", temp)
        i += 1

t2 = test2()
#直接调用send
#t2.send("hello world")#can't send non-None value to a just-started generator

#t2.send()#TypeError: send() takes exactly one argument (0 given)

print(t2.send(None))#与第一次调用__next__()效果一样
print(t2.send("hello world"))
print(t2.__next__())


print("*="*20, "send test3", "*="*20)
temp = "initial value"
def test3():
    global temp
    i = 0
    while i < 5:
        print("i = %d" % i)
        print("before : temp =", temp)
        if i % 2 == 0:
            temp = yield 0
        else:
            yield i
        print("after :temp =", temp)
        i += 1

t3 = test3()
print("+="*5, "first", "+="*5)
print(t3.send(None))

print("+="*5, "second", "+="*5)
print(t3.send("hello world"))

print("+="*5, "third", "+="*5)
print(t3.__next__())

print("+="*5, "fouth", "+="*5)
print(t3.__next__())

print("+="*5, "fifth", "+="*5)
print(t3.__next__())