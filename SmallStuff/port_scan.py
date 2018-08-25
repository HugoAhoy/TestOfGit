import socket as sk
def port_scan(ip, port_interval):
    for i in range(port_interval[0],port_interval[1] + 1):
        s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        print("IP:",ip,"  PORT", i,end ="")
        if s.connect_ex((ip,i) == 0:
            print(" OPEN ")
        else:
            print(" CLOSE")
        s.close()

if __name__ == '__main__':
    ip = input('Please input the ip address(IPv4):')
    port = input('Please input the interval of ports:(use brackets and comma):')
    port = port[1:-1]
    port = list(map(int,port.split(',')))
    port_scan(ip,port)