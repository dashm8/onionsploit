

class optsparser():

    def __init__(self):
        self.opts = {}
        self.notmend = {}

    def addopt(self,name):
        self.opts[name] = ""

    def addmend(self,opt):
        self.opts[opt] = ""


    def addopts(self,opts):
        self.opts += opts


