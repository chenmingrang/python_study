"""
TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
"""

import socket
#创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 7011))
print('Bind UDP on 7011')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % (addr, data.decode('utf-8')))
    s.sendto(b'Hello, %s' % data, addr)
