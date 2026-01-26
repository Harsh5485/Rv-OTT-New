@echo off
echo 🚀 Installing Koyeb CLI...

REM Download and install Koyeb CLI
echo Downloading Koyeb CLI...
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/koyeb/cli/releases/latest/download/koyeb-windows-amd64.exe' -OutFile 'koyeb.exe'"

REM Add to PATH temporarily
set PATH=%PATH%;%CD%

echo ✅ Koyeb CLI installed successfully!
echo.
echo Now run: koyeb login
echo Then: deploy-koyeb-manual.bat
pause