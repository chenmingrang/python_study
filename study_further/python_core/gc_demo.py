#gc垃圾回收机制1：引用计数机制
"""
python里每一个元素都是对象，它们的核心就是一个结构体：PyObject
typedef struc_object{
    int ob_refcnt;--引用计数
    struct_typeobject *ob_type;
}PyObject;

gc回收机制：引用计数机制为主，当为0时，对象会被回收，但是无法解决循环应用

"""

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

gc.disable()
f2()