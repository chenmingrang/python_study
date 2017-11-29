#gc垃圾回收机制2：隔代和分代回收为辅，三条列表
import gc
print(gc.get_count())
print(gc.get_count())
print(gc.get_count())
#(700, 10, 10)700新创建的对象减已释放的对象值大于700即对零代回收，10：每清理10次零代清一次一代顺带清理零代，10：每清理10次一代清理一次二代，顺带清理零代和一代
print(gc.get_threshold())
print(gc.get_threshold())
print(gc.get_threshold())

import  gc
class ClassA():
    def __init__(self):
        print("object bron, id : %s" % str(hex(id(self))))

#引用计数无法解决此类情况，环引用，内存持续增大
def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        print("----1-----")
        print(gc.garbage)
        print("----2----")
        gc.collect()
        print('----3----')
        print(gc.garbage)
        print('----4----')

gc.disable()
f2()