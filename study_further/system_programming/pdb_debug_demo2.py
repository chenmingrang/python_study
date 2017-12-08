import pdb
def avg(a, b):
    result = a + b
    print(result//2)
    return result//2

pdb.run('avg(10, 20)')

def f1():
    a = 10
    b = 20
    pdb.set_trace()
    c = (a + b)//2
    print(c)
    return c

print(f1())