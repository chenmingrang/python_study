class Money(object):

    def __init__(self):
        self.__num = 0

    @property#确定了属性名以及方法名
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        self.__num = newNum

a = Money()
a.num = 10000
print(a.num)
print(a._Money__num)