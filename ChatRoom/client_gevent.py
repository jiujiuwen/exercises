#!/usr/bin/env python
# coding=utf8
# client

from gevent import socket, monkey, select
import sys
import gevent

class FdReadable:
    def __init__(self):
        pass

    def readable(self, fd):
        rlist, _, _ = select.select([fd], [], [], 0) #不阻塞
        if rlist:
            return True
        return False

class CMsgHandler:
    def __init__(self, sock):
        self.sock = sock

    def get_input(self):
        msg = raw_input()
        return msg

    def send(self):
        msg = self.get_input()
        self.sock.sendall(msg)
        if msg == "exit":
            self.sock.close()
            sys.exit()

    def receive(self):
        try:
            all_msg = self.sock.recv(1024)
        except Exception:
            print("recieve ERROR")
            self.sock.close()
            sys.exit()
        else:
            print(all_msg)
            # ip_port =  ''.join(all_msg.split(":")[:-1])
            # msg = all_msg.split(":")[-1]
            # if msg:#空消息不打印
            #
            #     print("{ip_port}:{msg}".format(ip_port=ip_port, msg=msg))

class ChatClient(CMsgHandler):
    def __init__(self, sock, host, port):
        CMsgHandler.__init__(self, sock)
        self.r = FdReadable()
        self.host = host
        self.port = port

    def connection(self):
        try:
            self.sock.connect((self.host, self.port))
        except socket.error as e:
            print("start client ERROR . {}".format(e))
            sys.exit()
        print(self.sock.recv(1024).decode('utf-8'))  # 连接之前，server发来的消息

    def send(self):
        if self.r.readable(sys.stdin): #本地有输入
            CMsgHandler.send(self)

    def receive(self):
        if self.r.readable(self.sock): #自己可读
            CMsgHandler.receive(self)


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 9990

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = ChatClient(sock, HOST, PORT)
    #建立连接
    client.connection()

    #添加协程
    monkey.patch_all()
    while 1:
        gevent.joinall([
            gevent.spawn(client.send)
            , gevent.spawn(client.receive)
        ])



