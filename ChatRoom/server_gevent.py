#!/usr/bin/env python
# coding=utf8
# tcp StreamServer
from gevent.server import StreamServer
from gevent.lock import Semaphore
import time
import sys


class ClientHandler:
    def __init__(self):
        self.client_list = []
        self.sem = Semaphore()

    def get_num(self):
        return len(self.client_list)

    def get_clients(self):
        return self.client_list

    def add(self, user):
        self.sem.acquire()
        self.client_list.append(user)
        self.sem.release()
        # print(self.client_list)

    def remove(self, user):
        self.sem.acquire()
        self.client_list.remove(user)
        self.sem.release()
        if len(self.client_list) == 0:
            key_in = raw_input(
                "[ Notice ] No one left.input any to continue OR 'exit' to exit... ")
            if key_in == "exit":
                sys.exit()


class SMsgHandler:
    def __init__(self, sock, addr, client_obj):
        self.sock = sock
        self.addr = addr
        self.client_obj = client_obj
        self.time = time.strftime("%H:%M", time.localtime())  # 冒号
        self.prefix_info = "{time} {ip}<{port}>".format(
            time=self.time, ip=self.addr[0], port=self.addr[1])

    def broadcast_msg(self, msg):
        for s in self.client_obj.get_clients():
            s.sendall(
                "{prefix}:{msg}".format(
                    prefix=self.prefix_info,
                    msg=msg))

    def local_print(self, msg):  # msg 发送的内容
        print("{prefix}:{msg}".format(prefix=self.prefix_info, msg=msg))

    def when_receive(self, msg):
        # if msg:
        self.local_print(msg)
        self.broadcast_msg(msg)


class ChatServer(SMsgHandler):
    def __init__(self, sock, addr, client_obj):
        SMsgHandler.__init__(self, sock, addr, client_obj)
        self.in_info = "[ Notice ] Come in.".format(
            ip=self.addr[0], port=self.addr[1])
        self.out_info = "[ Notice ] Exited.".format(
            ip=self.addr[0], port=self.addr[1])
        self.welcome_info = "[ Notice ] Welcome! You're {ip}<{port}>.".format(
            ip=self.addr[0], port=self.addr[1])

    def add_client(self):
        client_num = self.client_obj.get_num() + 1
        self.sock.send("{} TOTAL {}.".format(self.welcome_info, client_num))
        SMsgHandler.when_receive(
            self, "{} TOTAL {}.".format(
                self.in_info, client_num))  # 本地打印 + 广播
        self.client_obj.add(self.sock)

    def run(self):
        while True:
            data = self.sock.recv(1024)
            #SMsgHandler.revieve(self, data)
            if data == "exit":
                client_num = self.client_obj.get_num() - 1
                SMsgHandler.when_receive(
                    self, "{} {} LEFT.".format(
                        self.out_info, client_num))
                self.client_obj.remove(self.sock)  # recieve 之后remove
                self.sock.close()
                break
            SMsgHandler.when_receive(self, data)  # exit不发送


def handler(sock, addr):
    global client_obj
    server = ChatServer(sock, addr, client_obj)
    server.add_client()
    server.run()


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 9990
    print("<ChartRoom Server>")

    client_obj = ClientHandler()
    try:
        s = StreamServer((HOST, PORT), handler)
        s.serve_forever()
    except Exception as e:
        print("start server ERROR . {}".format(e))
        sys.exit()
