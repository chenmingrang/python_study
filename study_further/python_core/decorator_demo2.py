def makeBold(fn):
    def wrapped():
        return "<b>" + fn() +"</b>"
    return wrapped

def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world"

@makeItalic
def test2():
    return "say hi"

print(test1())
print(test2())

@makeItalic
@makeBold
def test3():
    return "HELLO WORLD"
print(test3())

@makeBold
@makeItalic
def test4():
    return "HELLO WORLD"

print(test4())