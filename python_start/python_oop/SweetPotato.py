class SweatPotato:

    def __init__(self):
        self.cookedLevel = 0
        self.desc = '生的'
        self.condiments = []

    def cook(self,time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.desc = "糊了"
        elif self.cookedLevel > 5:
            self.desc = "熟了"
        elif self.cookedLevel > 3:
            self.desc = "夹生"

    def addCondiments(self,condiment):
        self.condiments.append(condiment)

    def printInfo(self):
        print("生熟情况：%s ； 调料：%s" % (self.desc,"，".join(self.condiments)))

    def __str__(self):
        msg = "生熟情况：%s ； 调料：%s" % (self.desc,"，".join(self.condiments))
        return msg

p1 = SweatPotato()
print("---2min---")
p1.cook(2)
print("---+香油---")
p1.addCondiments("香油")
print(p1)

print("---2min---")
p1.cook(2)
print("---+辣椒酱---")
p1.addCondiments("辣椒酱")
p1.printInfo()

print("---2min---")
p1.cook(2)
print(p1)

print("---4min---")
p1.cook(4)
print(p1)




