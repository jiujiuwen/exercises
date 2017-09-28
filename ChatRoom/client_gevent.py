#!/usr/bin/env python
# coding=utf8
# server

from gevent import socket, monkey, select
import sys
import gevent


class ChatClient:
    def __init__(self, sock):
        self.sock = sock

    def send(self):
        rlist, _, _ = select.select([sys.stdin], [], [], 0.5) #有标准输入，超时时间0.5
        if rlist:
            msg = raw_input()
            self.sock.sendall(msg)
            if msg == "exit":
                self.sock.close()
                sys.exit()

    def receive(self):
        global s
        rlist, _, _ = select.select([s], [], [], 0.5) #other
        if rlist:
            try:
                all_msg = self.sock.recv(1024)
            except Exception:
                print("revieve error")
                self.sock.close()
                sys.exit()
            else: #有消息
                ip_port = all_msg.split(":")[0]
                msg = all_msg.split(":")[-1]
                if msg:  # 空信息不打印
                    out_info = "{ip_port}:{msg}".format(ip_port=ip_port, msg=msg)
                    print(out_info)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(('127.0.0.1', 9990))
    except socket.error as e:
        print("check port. Error:%s" % e)
        sys.exit()
    print(s.recv(1024).decode('utf-8'))# reveive ID information

    client = ChatClient(s)
    monkey.patch_all()

    while 1:
        gevent.joinall([
            gevent.spawn(client.send)
            , gevent.spawn(client.receive)
        ])



