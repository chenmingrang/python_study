#生成器generator
a = [x for x in range(10)]
print(a)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#需要很大的一个列表，但又不占用很大的空间


#生成器方式1[将[] 改为 ()]
print("*="*15, "generator1", "*="*15)
b = (x for x in range(10))
print(b)#<generator object <genexpr> at 0x0000018EB7F3F780>
print(next(b))


#生成器2（菲波那切数列）
print("*="*15, "generator2", "*="*15)
#1 1 2 3 5 8 13 21 24
m, n = 0, 1
m, n = n, m + n
print(m, n)#1 1
m, n = n, m + n
print(m, n)#1 2
m, n = n, m + n
print(m, n)#2 3
m, n = n, m + n
print(m, n)#3 5

def fib():
    a, b = 0, 1
    for i in range(10):
        a, b = b, a+b
        print(b)
fib()#如果需要保存生成的值，可能需要很大的列表

def fib():
    print("======strat=======")
    a, b = 0, 1
    for i in range(10):
        print("======1=======")
        yield b#调用一次，遇到yield程序会停止，返回b
        print("======2=======")
        a, b = b, a+b
    print("======stop=======")
func = fib()#无输出
print(func)#<generator object fib at 0x000001C10F63FFC0>
#后面的调用是建立在之前调用的基础上的
num = next(func)#======strat=======
print(num)#1
num = next(func)
print(num)#1
num = next(func)
print(num)#2
num = next(func)
print(num)#3
