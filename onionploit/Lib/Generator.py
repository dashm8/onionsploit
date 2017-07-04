class Generator:
    
    def __init__(self,payload,port,addr,outfile="payload.py"):
        self.payload = payload
        self.port = port
        self.addr = addr
        self.outfile = outfile

    def createPaylad(self):
        counter = 0
        f = open(self.outfile,'w')
        for lines in open(payload):
            if lines.statswith("#const"):
                counter = 2
                continue
            if counter == 2:
                f.write("OnionUrl = " + self.addr)
                continue
            if counter == 1:
                f.write("PORT = " + self.port)
                continue
            f.write(lines)
        f.close()

class compiler:
    def __init__(self,infile,outfileformat,os):
        print("hopefully do stuff")
            
    
