
#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
def foo(s):
    n = int(s)
    assert n ==0, 'n is zero!'
    print(n)
    return 10/n

import logging
logging.basicConfig(level=logging.ERROR)

#使用logging来记录运行日志
def log_test():
    n = 0
    logging.info('n = %d ' % n)
    try:
        print(10/n)
    except Exception as e:
        logging.error(e)

if __name__=='__main__':
    """
        如果断言失败，assert语句本身就会抛出AssertionError
        启动Python解释器时可以用-O参数来关闭assert,关闭后，你可以把所有的assert语句当成pass来看（忽略断言）
    """
    #foo('3')
    #日志输出到控制台
    log_test()


