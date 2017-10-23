import socket, threading

def gen_sock():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 7011))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Micheal', b'Tim', b'Tom']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

for i in range(50):
    t = threading.Thread(target=gen_sock ,name="thread"+str(i))
    t.start()