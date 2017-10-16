#collections是Python内建的一个集合模块，提供了许多有用的集合类。
print("*="*10, 'namedtuple', '*='*10)
#tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成。
#但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
p = (1, 2)
print(p)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print('p.x = %s p.y = %s ' % (p.x, p.y))
#p.x = 10#AttributeError: can't set attribute


#p2 = Point(1, 2, 3)#takes 3 positional arguments but 4 were given
"""
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
"""
print(isinstance(p, Point))#True
print(isinstance(p, tuple))#True


print("*="*10, 'deque', '*='*10)
"""
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
"""

from collections import deque

dq = deque(['a', 'b', 'c'])
dq.append('x')
dq.appendleft('y')
print(dq)#deque(['y', 'a', 'b', 'c', 'x'])


print("*="*10, 'defaultdict', '*='*10)

"""
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
"""

from collections import defaultdict

dd = defaultdict(lambda : 'N/A')
dd['k1'] = 'abc'
dd['k2'] = 'def'
print(dd['k1'])#abc
print(dd['k3'])#N/A
#默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。


print("*="*10, 'OrderedDict', '*='*10)

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print(od)

#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


print("*="*10, 'Counter', '*='*10)
#Counter是一个简单的计数器，例如，统计字符出现的个数
#Counter实际上也是dict的一个子类
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)