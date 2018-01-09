import socket
from threading import Thread

up_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bind_addr = ('', 8999)
up_socket.bind(bind_addr)

def task1():
    # 接收消息
    while True:
        rec_data = up_socket.recvfrom(1024)
        print('receive "%s" from %s:%s' % (str(rec_data[0], "gb2312"), rec_data[1][0], rec_data[1][1]))

def task2():
    # 发送消息
    for i in range(10):
        up_socket.sendto(("你好201"+str(i)+"！").encode("gb2312"), ('192.168.238.1', 8080))

t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()