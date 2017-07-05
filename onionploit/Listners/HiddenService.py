import os
import sys


class HiddenService:

    def __init__(self,port,payload):
        self.port = port
        self.payload = payload
        self.pid = GetTorPid()
        os.system("kill " + pid)
        CreateHiddenService()
        self.hostname = GetHostName()

    def GetTorPid(self):
        open("tmp.txt", 'w').close()
        os.system("ps -A | grep -w tor >> tmp.txt")
        for lines in open('tmp.txt','r'):
            return lines[1:5]
        
    
    def CreateHiddenService(self):
        f = open("Sources/torrc",'r')
        os.system("cp /etc/tor/torrc /etc/tor/torrc.copy")
        os.system("rm /etc/tor/torrc")
        torrc = open("/etc/tor/torrc",'w')
        counter = 1
        for lines in f:
            if counter == 72:
                torrc.write("HiddenServiceDir ~/hidden_service/" + self.payload + "/")
            if counter == 73:
                torrc.write("HiddenServicePort "+self.port+" 127.0.0.1:"+self.port)
            else:
                torrc.write(lines)
        torrc.close()
        f.close()
        os.system("tor")

    def GetHostName(self):
        f = open("~/hidden_service/" + self.payload + "/")
        for line in f:
            return line


