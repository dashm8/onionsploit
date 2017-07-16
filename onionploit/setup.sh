sudo apt-get install wine
wine msiexec /i python-2.7.10.msi /L*v log.txt
cd ~/.wine/drive_c/Python27
wine python.exe Scripts/pip.exe install pyinstaller

