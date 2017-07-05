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