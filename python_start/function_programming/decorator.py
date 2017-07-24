def now():
    print('2017-7-4')

f =now
f()#2017-7-4
print(f.__name__)#now
print(now.__name__)#now

"""
假设我们要增强now()函数的功能，比如，
在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
"""

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-7-4')

"""
call now():
2017-7-4
"""

now()

now = log(now)
print(now)#<function log.<locals>.wrapper at 0x000001DEBF7A52F0>
print(now.__name__)#wrapper


def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

print("=======execute=======")
@log('execute')
def now():
    print('2017-7-5')

now()

print("=======log('execute')(now)=======")
f = log('execute')(now)
print(f.__name__)#wrapper
#f()


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator






