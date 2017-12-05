import functools
print(dir(functools))

#偏函数partial
print("*="*20, "partial", "*="*20)
def showarg(*args, **kw):
    print("args = %s; kw=%s" % (args, kw))

p1 = functools.partial(showarg, 1, 2, 3)
showarg(1, 2 , 3)
p1()
showarg(1, 2 , 3, 4, 5, 6)
p1(4, 5, 6)
showarg(1, 2 , 3, a="python", b="cmr")
p1(a="python", b="cmr")

p2 = functools.partial(showarg, a =3, b="python")
showarg(a =3, b="python")
p2()
showarg(1, 2, a =3, b="python")
p2(1, 2)
showarg(b="python", a="java", c="javascript")
p2(a="java", c="javascript")


#wraps
print("*="*20, "wraps", "*="*20)

def note(func):
    "note fucntion"
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print("I am test")

print(help(test))#装饰器的函数说明


def note2(func):
    "note fucntion"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note2
def test2():
    "test function"
    print("I am test2")

print(help(test2))#test2的方法说明