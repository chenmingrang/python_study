class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    pass

class Cat(Animal):
    pass


a = Animal()
b = Dog()
c = Cat()
a.run()#Animal is running
b.run()#Animal is running
c.run()#Animal is running


class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

a = Animal()
b = Dog()
c = Cat()
a.run()#Animal is running
b.run()#Dog is running
c.run()#Cat is running


print(isinstance(a,Animal))#True
print(isinstance(b,Animal))#True
print(isinstance(c,Animal))#True

print(isinstance(a,Dog))#False


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
'''
Dog is running
Dog is running
'''


#静态语言 vs 动态语言

class Timer(object):
    def run(self):
        print("Start...")


t = Timer()

run_twice(t)
'''
Start...
Start...
'''
#run_twice方法接收的对象只要有run方法就可以，不需要非得是animal类型

run_twice(int('123'))#AttributeError: 'int' object has no attribute 'run'

