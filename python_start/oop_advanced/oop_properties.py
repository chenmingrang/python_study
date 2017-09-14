class Tool(object):
    #类属性
    num = 0
    #方法
    def __init__(self,tool_name):
        #对象属性
        self.name = tool_name
        Tool.num += 1


tool1 = Tool('铁锹')
tool2 = Tool('水桶')
tool3 = Tool('瓢')
print(tool3.num)#3
print(Tool.num)#3

print("*="*20)

class Game(object):
    #类属性
    num = 0
    #实例方法
    def __init__(self):
        self.name = 'xxx'

    #类方法（必须要一个参数）
    @classmethod
    def add_num(cls):
        cls.num += 100

    #静态方法(可以不需要参数)
    @staticmethod
    def print_menu():
        print("-"*10)
        print("======开始游戏======")
        print("-"*10)

game = Game()
#Game.add_num()
game.add_num()#实例也可以调用类方法
print(Game.num)#100
Game.print_menu()
game.print_menu()




