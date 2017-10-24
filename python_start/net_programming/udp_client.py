import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Micheal', b'Tom', b'Lucy']:
    s.sendto(data, ('127.0.0.1', 7011))
    print(s.recv(1024).decode('utf-8'))
s.close()