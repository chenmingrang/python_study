"""
在Thread和Process中，应当优选Process，因为Process更稳定，
而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
"""
import time, queue

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    ## 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
    QueueManager.register('get_task')
    QueueManager.register('get_result')

    #连接到服务器，也就是运行task_master.py的机器
    server_ip = '127.0.0.1'
    print('Connet to server %s...' % server_ip)
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    m = QueueManager(address=(server_ip,5000),authkey=b'abc')
    m.connect()
    print('connect successfuly')

    #获取queue对象
    task = m.get_task()
    result = m.get_result()

    #从task队列获取任务，并把结果写入result队列
    for i in range(5):
        try:
            n = task.get(timeout=1)
            print('run task %d*%d...' % (n, n))
            time.sleep(1)
            result.put(n * n)
        except queue.Empty:
            print("task queue is empty")
    print('worker exit.')





