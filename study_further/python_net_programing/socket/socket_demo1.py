import socket

#ipv4 tcp
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ipv4 udp
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#发消息
send_addr = ("192.168.238.1", 8080)
s_udp.sendto(b"hello world", send_addr)

rec_data = s_udp.recvfrom(1024)
print('receive "%s" from %s:%s' % (str(rec_data[0], "utf-8"), rec_data[1][0], rec_data[1][1]))

s_udp.close()