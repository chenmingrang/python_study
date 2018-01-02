from multiprocessing import Pool, freeze_support
import time, os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--" % (os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---" % i)
        time.sleep(1)
    return "hello"

def test2(args):
    print("---callback func--pid=%d" % os.getpid())
    print("---callback func--args=%s" % args)
    time.sleep(1)
    print('sleep 1 second in callback')

if __name__ == '__main__':
    freeze_support()
    pool = Pool(3)
    #callback在子进程结束后，主进程立即执行，子进程的返回值为参数
    pool.apply_async(func=test,callback=test2)

    while True:
        time.sleep(1)
        print("----主进程-pid=%d----" % os.getpid())
