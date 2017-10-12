"""
在Thread和Process中，应当优选Process，因为Process更稳定，
而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
"""
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
result_queue = queue.Queue()
def return_task():
    return task_queue
def return_result():
    return result_queue
class QueueManager(BaseManager):
    pass
def test():
    QueueManager.register('get_task',callable = return_task)
    QueueManager.register('get_result',callable = return_result)
    # 绑定到端口5000,并且设置验证码'abc'
    manager = QueueManager(address = ('127.0.0.1',5000),authkey = b'abc')
    manager.start()

    # 获得通过网络访问的Queue对象
    task,result = manager.get_task(),manager.get_result()

    #放一些任务
    for i in range(5):
        n = random.randint(0, 10)
        print('put %d in task' % n)
        task.put(n)

    #获取结果
    print('try to get result')
    for i in range(5):
        r = result.get(timeout = 10)
        print('get the result %d' % r)

    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
    test()



