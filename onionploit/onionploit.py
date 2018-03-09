import os
import sys
from Listners.TCPServer import Server
import Lib.Generator
import sys
import miniupnpc

class Console:

    def run(self):
        while 1:
            try:
                inp = str(raw_input("onionsploit/>"))                            
                self.handle(inp)
            except Exception as e:
                # remove e on production
                print "[!] unknown error please try again"
                if os.path.isfile("/etc/tor/torrc.copy"):
                    os.system("sudo cp /etc/tor/torrc.copy /etc/tor/torrc")                
                print e

    def __init__(self):
        self.state = "start"
        self.run()

    def listpayloads(self):
        for path,subdirs,files in os.walk("Payloads/"):
            for name in files:
                print os.path.join(path,name)

    def helpscreen(self):
        help = """
        set:
        \t sets the payload
        \t usage: set <payload_name>
        gen:
        \t generate a payload without a Server
        \t usage: gen <payload_name>
        list_payloads:
        \t will list all payloads avilable
        """
        return help

    def handle(self,inp):        
        if inp == "exit":
            print("[!] exiting !!!!")
            sys.exit()
        elif inp == "list_payloads":
            self.listpayloads()
        elif inp.startswith("set"):
            try:
                self.payload = "Payloads/" + inp.split(" ")[1]             
            except IndexError:
                print("[!] no payload was entered")
                return None
            if not os.path.isfile(self.payload):
                print("[!] no such payload") 
                return None
            self.state = "payloadoption"
            self.setoption()
        elif inp.startswith("gen"):
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
            g = Generator.Generator(self.payload,raw_input("enter port: "),raw_input("enter .onion url: "),opts)
        elif "help" in inp:
            print self.helpscreen()
            return None
        else:
            print "[!] command not found: "
            return None

    def setoption(self):
        rport = 0
        service = "new"
        while 1:
            cmd = raw_input(self.payload + ">")
            if cmd == "help":
                print "enter: \t rport=<your_port>"
                print "enter: \t newservice=False if you already have a tor service running with our server"
            elif cmd == "exploit":
                if rport != 0:
                    print("[+] starting exploit at: " +  str(rport))
                    if len(sys.argv) != 1 and sys.argv[1] == "-upnp":
                        self.mapport(rport)
                    s = Server(rport,self.payload,service)
                    s.run()
                else:
                    print("[!] you must enter a port number")
            elif cmd.startswith("rport =") or cmd.startswith("rport="):
                rport = int(cmd.split("=")[1])            
            elif cmd.startswith("newservice=") or cmd.startswith("newservice ="):
                service = "notnew"
            elif cmd == "exit":
                print("[!] exiting")
                return None
            else:
                print "[!] no such command"

    def mapport(self,port):
        u = miniupnpc.UPnP()
        u.discoverdelay = 200
        ndev = u.discover()
        print "[!] upnp-number of devices" + str(ndev)
        u.selectigd()
        b = u.addportmapping(port,'TCP',u.lanaddr,port,'UPnP IGD Tester port %u' % port,'')
        print "[+] upnp-port is mapped"


if os.getuid() !=0:
    print "you need sudo for that silly"
    sys.exit()
c = Console()
