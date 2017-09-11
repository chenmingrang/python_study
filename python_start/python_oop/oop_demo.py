class Home:

    def __init__(self,area):
        self.area = area
        self.items = []

    def __str__(self):
        desc = "可用面积：%d ；" % self.area +"现有家具："
        list1 = []
        for x in self.items:
            list1.append(x.type)
        return desc+",".join(list1)

    def add(self,item):
        if item.area <= self.area:
            self.items.append(item)
            self.area -= item.area

class Bed:
    def __init__(self,area,type):
        self.area = area
        self.type = type

    def __str__(self):
        return "%s 占地:%d" % (self.type,self.area)

home = Home(134)
print(home)

bed = Bed(4,"弹簧床")
print("添加一张弹簧床===》",bed)
home.add(bed)
print(home)

bed = Bed(5,"席梦思床")
print("添加一张席梦思床===》",bed)
home.add(Bed(5,"席梦思床"))
print(home)
