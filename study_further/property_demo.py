class Money(object):

    def __init__(self):
        self.__num = 0

    def setNum(self, newNum):
        print('===setNum===')
        self.__num = newNum

    def getNum(self):
        print('===getNum===')
        return self.__num

    #调用getNum和setNum方法,对方法进行简单的封装
    num = property(getNum, setNum)

a = Money()
a.num = 10000#调用a.setNum(10000)
print(a.num)#调用a.getNum()
print(a._Money__num)#10000 名称重整