#进程之间的通信，queue（队列，先进先出） stack(栈，后进先出)

from multiprocessing import Queue

#最多三个元素
q = Queue(3)
q.put("123")
q.put("abc")
q.put("xyz")
#队列已满，此处会阻塞
#q.put("lmn")
print(q.qsize())
print(q.get())
q.put("lmn")
print(q.qsize())
print(q.full())
print(q.empty())