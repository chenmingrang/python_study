class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


#给动物加上Runnable 和 Flyable的功能

class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("Flying..")


class Cat(Mammal,Runnable):
    pass

class BlueBird(Bird,Flyable):
    pass


#掺合模式（Mixin）: 通过多重继承，一个子类就可以同时获得多个父类的所有功能

#在设计类的时候，我们优先考虑通过多重继承来组合多个的功能，而不是设计多层次的复杂的继承关系
