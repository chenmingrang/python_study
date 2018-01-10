from socket import *

s  = socket(AF_INET, SOCK_DGRAM)
bind_addr = ("", 8999)

s.bind(bind_addr)

while True:
    rec_data = s.recvfrom(1024)
    print('receive "%s" from %s:%s' % (str(rec_data[0], "gb2312"), rec_data[1][0], rec_data[1][1]))
    s.sendto(rec_data[0], rec_data[1])
    if str(rec_data[0],'gb2312') == "exit":
        s.sendto(b'bye bye', rec_data[1])
        s.close()
        break
print('socket is closed!')