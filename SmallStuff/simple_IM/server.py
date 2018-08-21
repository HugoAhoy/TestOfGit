import socket 
import threading
import re



def data_parser(data):
    if data == b'exit':
        return True
    else:
        pass


def tcplink(sock, addr):
    print("create new thread from%s:%s"%addr)
#receive message
    total_data = []
    while True:
        data = sock.recv(1024)
        if not data:
            break
        total_data.append(data)
#process message
    data_parser(total_data)





if __name__ = '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9999))
    s.listen(12)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
    