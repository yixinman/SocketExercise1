import socket,sys

host = '127.0.0.1'
port = 3333

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.send("Hello")
s.shutdown(1)

while True:
    buf = s.recv(1024)
    sys.stdout.write(buf)
