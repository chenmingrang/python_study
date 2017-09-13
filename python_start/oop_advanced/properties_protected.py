class Person:
    #私有方法
    def __f1(self):
        print("****f1****")

    def f2(self):
        print("*****f2****")

    def f3(self):
        print("私有方法f1被调用!")
        self.__f1()

p = Person()
#p.__f1()#'Person' object has no attribute '__f1'
p.f2()
p.f3()





