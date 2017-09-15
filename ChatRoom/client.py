#!/usr/bin/env python
#coding=utf8
#server

import socket
import threading
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.connect(('127.0.0.1', 9990))
except socket.error as e:
    print("check port. Error:%s"%e)
    sys.exit()

class ChatClient:
    def __init__(self,sock):
        self.sock = sock

    def send(self):
        while 1:
            msg = raw_input()
            self.sock.sendall(msg)
            #print(self.sock.recv(1024).decode('utf-8'))
            if msg == "exit":
                sys.exit()

    def receive(self):
        while 1:
            all_msg = self.sock.recv(1024)
            ip_port = all_msg.split(":")[0]
            msg = all_msg.split(":")[-1]

            print("{ip_port}:{msg}".format(ip_port=ip_port,msg=msg))
            if msg == "exit":
                sys.exit()

client= ChatClient(s)
#reveive ID information
print(s.recv(1024).decode('utf-8'))
t1 = threading.Thread(target=client.send)
t2 = threading.Thread(target=client.receive)
t1.start()
t2.start()