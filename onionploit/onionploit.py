import os
import sys
from Listners.TCPServer import Server
import Lib.Generator

class Console:
    def run(self):
        while 1:
            self.handle(input("onionsploit/>"))

    def __init__(self):
        self.state = "start"
        self.run()

    def listpayloads():
        for files in os.listdir("~/Payloads/"):
            print(files)

    def handle(self,inp):        
        if inp == "exit":
            print("[!] exiting !!!!")
            sys.exit()
        if inp == "list payloads":
            listpayloads()
        if inp.startswith("set"):
            try:
                self.payload = inp.split(" ")[1]             
            except IndexError:
                print("[!] no payload was entered")
                return None
            if not os.path.isfile(self.payload):
               print("[!] no such payload") 
               return None
            self.state = "payloadoption"
            self.setoption()
        if inp.startswith("gen"):
            data = input("[!] do you want to compile the python payload(y:n) ")
            if data == "y":
                opts = {"compile" : True}
            if data == "n":
                opts = {"compile" : False}
            try:
                self.payload = inp.split(" ")[1]
            except IndexError:
                print("[!] no payload was entered")
                return None
            if not os.path.isfile(self.payload):
                print("[!] no such payload")
                return None
            g = Generator.Generator(self.payload,input("enter port: "),input("enter .onion url: "),opts)

    def setoption(self):
        rport = 0
        while 1:
            cmd = input(self.payload + ">")
            if cmd == "exploit":
                if rport != 0:
                    print("[+] starting exploit at: " +  str(rport))                    
                    s = Server(rport,self.payload)
                    s.run()
                else:
                    print("[!] you must enter a port number")
            if cmd.startswith("rport =") or cmd.startswith("rport="):
                rport = int(cmd.split("=")[1])            
            if cmd == "exit":
                print("[!] exiting")
                return None




c = Console()