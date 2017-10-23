"""
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可.
"""

#基于tcp连接的Socket

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4 面向流的TCP协议
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection:Keep-Alive\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('baidu.html', 'wb') as f:
    f.write(html)