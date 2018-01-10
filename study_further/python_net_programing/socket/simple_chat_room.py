import socket
from threading import Thread

def receive_data(udp_socket):
    # 接收消息
    while True:
        rec_data = udp_socket.recvfrom(1024)
        print('>>receive "%s" from %s:%s' % (str(rec_data[0], "gb2312"), rec_data[1][0], rec_data[1][1]))
        print("\n<<")

def send_data(udp_socket):
    # 发送消息
    while True:
        msg = input("请输入发送的内容：")
        udp_socket.sendto(("<< %s" % msg).encode("gb2312"), ('192.168.238.1', 8080))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8999))

    t_rece = Thread(target= receive_data, args=(udp_socket,))
    t_send = Thread(target= send_data, args=(udp_socket,))

    t_rece.start()
    t_send.start()

    t_rece.join()
    t_send.join()

if __name__ == "__main__":
    main()