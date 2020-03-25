import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 50000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    msg = raw_input("daj chleb: ")
    s.send(msg)
    data = s.recv(BUFFER_SIZE)
    print "received data:", data
    
s.close()

print "received data:", data