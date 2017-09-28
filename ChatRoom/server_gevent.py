#!/usr/bin/env python
# coding=utf8
# tcp StreamServer
from gevent.server import StreamServer
import time
import sys

class ClientHandler:
    def __init__(self):
        self.client_list = []

    def get_num(self):
        return len(self.client_list)

    def get_clients(self):
        return self.client_list

    def add(self, user):
        self.client_list.append(user)
        #print(self.client_list)

    def remove(self, user):
        self.client_list.remove(user)
        if len(self.client_list) == 0:
            key_in = raw_input("[ Notice ] No one left.input any to continue OR 'exit' to exit... ")
            if key_in == "exit":
                sys.exit()

class MsgHandler:
    def __init__(self, sock, addr, client_obj):
        self.sock = sock
        self.addr = addr
        self.client_obj = client_obj
        self.time = time.strftime("%H.%M.%S", time.localtime()) #冒号
        self.prefix_info = "{time} {ip}<{port}>".format(time=self.time, ip=self.addr[0], port=self.addr[1])

    def broadcast_msg(self, msg):
        for s in self.client_obj.get_clients():
            s.sendall("{prefix}:{msg}".format(prefix=self.prefix_info,msg=msg))

    def local_print(self, msg): #msg 发送的内容
        print("{prefix}:{msg}".format(prefix=self.prefix_info,msg=msg))

    def revieve(self, msg):
        #if msg:
        self.local_print(msg)
        self.broadcast_msg(msg)

class ChatServer(MsgHandler):
    def __init__(self, sock, addr, client_obj):
        MsgHandler.__init__(self, sock, addr, client_obj)
        self.in_info = "[ Notice ] Come in. Totol {num}.".format(ip=self.addr[0], port=self.addr[1], num=self.client_obj.get_num()+1)
        self.out_info = "[ Notice ] Exited. {num} left".format(ip=self.addr[0], port=self.addr[1], num=self.client_obj.get_num())
        self.welcome_info = "[ Notice ] Welcome! You're {ip}<{port}>.".format(ip=self.addr[0], port=self.addr[1])

    def add_client(self):
        self.sock.send(self.welcome_info)
        MsgHandler.local_print(self, self.in_info)
        MsgHandler.broadcast_msg(self, self.in_info)
        # MsgHandler.revieve(self, self.in_info)
        self.client_obj.add(self.sock)

    def run(self):
        while 1:
            data = self.sock.recv(1024)
            MsgHandler.revieve(self, data)
            if data == "exit":
                MsgHandler.revieve(self, self.out_info)
                self.client_obj.remove(self.sock) #recieve 之后remove
                self.sock.close()
                break

def handler(sock, addr):
    global client_obj
    server = ChatServer(sock, addr, client_obj)
    server.add_client()
    server.run()

if __name__ == "__main__":
    print("<ChartRoom Server>")
    client_obj = ClientHandler()
    s = StreamServer(('localhost', 9990), handler)
    s.serve_forever()
