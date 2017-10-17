#在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们
#正确关闭文件资源的一个方法是使用try...finally
#encoding=utf-8
try:
    f = open('./base64_module.py', 'r', encoding='utf-8')
    print(f.readline(30))
finally:
    if f:
        f.close()

print('*='*10, 'with', '*='*10)
#写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为
with open('./base64_module.py', 'r', encoding='utf-8') as f:
    print(f.readline(20))


"""
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的
"""

class Query(object):

    def __init__(self, name):
        self.name =name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s..' % self.name)

with Query('Tom') as q:
    q.query()


#编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下
print('*='*10, '@contextmanager', '*='*10)

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name= name

    def query(self):
        print('Query info about %s..' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Jackson') as q:
    q.query()


#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' %name)

with tag('h1'):
    print('hello')
    print('world')



print('*='*10, '@closing', '*='*10)
#如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    n = 1
    for line in page:
        if n==10:
            break
        n += 1
        print(line)

"""
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
#它的作用就是把任意对象变为上下文对象，并支持with语句
"""

