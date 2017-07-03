import os
import threading
class Console:
    def __init__(self):
        self.state = "start"
            
    def handle(self,inp):
        if inp.startswith("set"):
            try:
                self.payload = inp.split(" ")[1]
            except IndexError:
                print("[!] no payload was entered")
            if not os.path.isfile(self.payload):
               print("[!] no such payload") 
            self.state = "payloadoption"
            
    def setoption(self):
        rport = 0
        while 1:
            cmd = input(self.payload + ">")
            if cmd == "exploit":
                if rport != 0:
                    print("[!] starting exploit at: " +  str(rport))
                    


