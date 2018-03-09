import os
import sys
from time import sleep

class HiddenService:

    def __init__(self,port,payload):
        self.port = port
        self.payload = payload
        self.pid = self.GetTorPid()
        os.system("kill " + str(self.pid))
        print "[+] killed other tor services"
        self.CreateHiddenService()
        print "[+] new tor service created"
        self.hostname = self.GetHostName()
        print "[+] service hostname: " + self.hostname

    def GetTorPid(self):
        print "[+] getting tor pid"
        open("tmp.txt", 'w').close()
        os.system("ps -A | grep -w tor >> tmp.txt")
        for lines in open('tmp.txt','r'):
            print lines.split(" ")[0]
            return lines.split(" ")[0]
        
    
    def CreateHiddenService(self):
        print "[+] creating a hidden service"
        os.system("sudo cp /etc/tor/torrc /etc/tor/torrc.copy")
        f = open("/etc/tor/torrc",'a')        
        f.write("\n HiddenServiceDir /var/lib/tor/hidden_service/ \n")
        f.write("HiddenServicePort "+str(self.port)+" 127.0.0.1:"+str(self.port))        
        f.close()
        os.system("sudo rm -r /var/lib/tor/hidden_service/")
        os.system("mkdir /var/lib/tor/hidden_service")
        os.system("sudo chmod 700 /var/lib/tor/hidden_service/")
        os.system("tor")
        sleep(8)

    def GetHostName(self):
        f = open("/var/lib/tor/hidden_service/hostname")
        for line in f:
            return line.strip("\n")


