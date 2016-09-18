import socket,sys
import SocketServer

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ''
port = 3333


class RequestHandler(SocketServer.BaseRequestHandler): 
  def handle(self): 
    print '...connected from:', self.client_address 
    while True: 
        #sys.stdout.write("We get message reversed from the client:%s" %str((self.request.recv(1024))[::-1]))
        reversed = self.request.recv(1024)[::-1]
        self.request.sendall(reversed)
  
tcpServ = SocketServer.ThreadingTCPServer((host,port), RequestHandler) 
tcpServ.serve_forever()

    



