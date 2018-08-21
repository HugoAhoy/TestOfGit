from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',6666))
s.send(b'HELLOHUGO')
s.close()