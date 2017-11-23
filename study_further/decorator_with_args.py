#参数处理
def func(f):
    print("===func_1===")
    #def func_in():
    def func_in(*args, **kv):
        print("==func_in_before==")
        # f()
        f(*args, **kv)
        print("==func_in_after==")
    print("===func_2===")

    return func_in

@func
def test(a, b):
    print("in test:a=%s,b=%s" % (a, b))

#test(11, 22)#TypeError: func_in() takes 0 positional arguments but 2 were given
test(11, 22)

@func
def test_2(a, b, c):
    print("in test:a=%s,b=%s,c=%s" % (a, b, c))

test_2(11, 22, 33)