#!/usr/bin/env python
#coding=utf8
#server

import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9990))
s.listen(5)
print("<ChartRoom>")

global client_list
client_list = []

class SingleServer:
    def __init__(self,sock,addr):
        self.sock = sock
        self.addr = addr

    def broadcast_msg(self,sock,msg):
        for s in client_list: #包括client自己
            #if s != sock:
            s.send(msg)

    def get_msg(self):
        Id = "%s:%s" % self.addr
        self.broadcast_msg(self.sock, "%s Come in." % Id) #广播客户端
        print("%s Come in." % Id) #server端显示
        self.sock.send("Welcome!You're %s" % Id)
        client_list.append(self.sock)

        while True:
            data = self.sock.recv(1024)
            msg = "{ip}<{port}>:{msg}".format(ip=self.addr[0],port=self.addr[1],msg=data)
            print(msg)
            if data == 'exit':
                break
            self.broadcast_msg(self.sock,msg)
            #self.sock.send(msg)
        self.sock.close()
        self.broadcast_msg(self.sock, "Connection from %s:%s closed." % self.addr)
        print("Connection from %s:%s closed." % self.addr)
        #return msg


class ChatServer:
    def __init__(self):
        pass

    def run(self,sock,addr):
        s_server = SingleServer(sock, addr)
        s_server.get_msg()

server = ChatServer()
while 1:
    sock,addr = s.accept()
    t1 = threading.Thread(target=server.run, args=(sock, addr))
    t1.start()