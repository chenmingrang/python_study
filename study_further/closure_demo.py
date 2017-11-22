#闭包
def test():
    print("------test--------")

#加括号表示调用
#不加括号表示一个变量，指向函数
test()
print(test)#<function test at 0x000001F7DAB02048>

#与test指向同一个对象
b = test
print(b)#<function test at 0x000001F7DAB02048>

#相当于调用test(test())
b()


print("*="*15, 'closure', '*='*15)
#函数内部再定义一个函数，并且里面函数用到了外面函数的变量，那么将这个函数以及用到的一些变量称之为闭包
def outer(num1):

    print("--1--")

    def inner(num2):
        print("outer:%d + inner:%d =%d " % (num1, num2, num1+num2))

    print("--2--")

    return inner


a = outer(100)
print(a)#<function outer.<locals>.inner at 0x000002816E8C2268>
a(12)
a(23)