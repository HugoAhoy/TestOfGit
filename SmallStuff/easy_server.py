import threading
from socket import *
def tcplink(sock, addr):
    print("create new thread from%s:%s"%addr)
#receive message
    total_data = []
    while True:
        data = sock.recv(1024)
        if not data:
            break
        total_data.append(data)
        print(total_data)
        datastr  = b''.join(total_data).decode('utf-8')
        print(datastr)
'''
    f = open("/home/hugo/data_recv","w")
    f.write(''.join(total_data))
    f.close()
'''

s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1",6666))
s.listen(12)