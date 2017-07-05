import os
import sys
import Server
import Generator

class Console:
    def __init__(self):
        self.state = "start"
        while 1:
            handle(input(">"))
    def handle(self,inp):        
        if inp == "exit":
            print("[!] exiting !!!!")
            sys.exit()
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
            setoption()
        if inp.startswith("gen"):
            try:
                self.payload = inp.split(" ")[1]
            except IndexError:
                print("[!] no payload was entered")
                return None
            if not os.path.isfile(self.payload):
                print("[!] no such payload")
                return None
            g = Generator.Generator(self.payload,input("enter port: "),input("enter .onion url: "))

    def setoption(self):
        rport = 0
        while 1:
            cmd = input(self.payload + ">")
            if cmd == "exploit":
                if rport != 0:
                    print("[+] starting exploit at: " +  str(rport))                    
                    s = Server.Server(rport,self.payload)
                    s.run()
                else:
                    print("[!] you must enter a port number")
            if cmd.startswith("rport =") or cmd.startswith("rport="):
                rport = int(cmd.split(" ")[1])
            if cmd == "exit":
                print("[!] exiting")
                return None

