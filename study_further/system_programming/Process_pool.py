from multiprocessing import Pool
import os, random, time

def worker(msg):
    t_start = time.time()
    print('%s开始执行，进程号为%d' % (msg, os.getpid()))
    time.sleep(random.randint(1, 3))
    t_stop = time.time()
    print('%s执行完毕，耗时%0.2f' % (msg, t_stop -t_start))

if __name__ == '__main__':
    po=Pool(3) #定义一个进程池，最大进程数3
    #异步执行
    print("=" * 20 + "异步执行" + "=" * 20)
    for i in range(0,10):
        #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
        #每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))

    print("----start----")
    po.close() #关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")

    #同步处理
    print("="*20+"同步执行"+"="*20)
    po2 = Pool(4)
    for i in range(10):
        po2.apply(worker, (i,))
    # print("----start----")
    # po.close()  # 关闭进程池，关闭后po不再接收新的请求
    # po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后