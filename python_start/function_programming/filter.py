#Python内建的filter()函数用于过滤序列。
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    if isinstance(n,(int)):
       return n%2==1
    if n in ["b","d","f"]:
        return False
    return True

print(list(filter(is_odd,[1,2,3,4])))#[1, 3]
print(list(filter(is_odd,"abcdef")))#['a', 'c', 'e']

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,["A","","B",None,"C","  "])))#['A', 'B', 'C']

"""
    用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
    filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
"""





