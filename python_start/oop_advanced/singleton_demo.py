class Dog(object):
    __instance = None

    def __init__(self,name):
        self.name = name

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

d1 = Dog("d1")
print(d1.name)#d1
d2 = Dog("d2")
print(d2.name)#d2
print(d1.name)#d2
print(id(d1))#2199906996800
print(id(d2))#2199906996800

























