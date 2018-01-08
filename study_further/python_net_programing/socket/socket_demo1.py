import socket

#ipv4 tcp
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ipv4 udp
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#发消息
send_addr = ("192.168.238.1", 8080)
s_udp.sendto(b"hello world", send_addr)
