"""
和客户端编程相比，服务器编程就要复杂一些。
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
"""

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 7011))
#Enable a server to accept connections.
s.listen(5)
print('Waiting from connect...')

def tcplink(sock, addr):
    print('Accept new connecting from %s:%s...' % addr)
    sock.send(b'Hello World!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



