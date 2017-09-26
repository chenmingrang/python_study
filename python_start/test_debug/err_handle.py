#try...except...finally...

def f1():
    try:
        print('try...')
        division = int(input("请输入除数："))
        r = 10 / division
        print('result:% -3.3f'%r)
    except ZeroDivisionError as e:
        print('execpt:',e)
    except ValueError as e:
        print('输入的值不能转化为整数。')
    else:
        print("正确计算出结果")
    finally:
        print('finally...')
    print('end')


def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def f2():
    try:
        bar('0')
    except Exception as e:
        print('except:',e)
    finally:
        print('finally')

def f3():
    bar(0)

#记录错误
import logging
def f4():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally')
    print('*='*30)

def FooError(ValueError):
    pass

def f5(s):
    try:
        n = int(s)
        if n == 0:
            raise FooError('0 不能做除数！')
        return 10/n
    except Exception as e:
        raise FooError('invalid value:%s '% s)


if __name__=='__main__':
    #f1()
    #f2()
    """
        异常传递：错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获
    """
    #f3()
    """
        使用logging同样是出错，但程序打印完错误信息后会继续执行，并正常退出
    """
    #f4()
    f5('a')












