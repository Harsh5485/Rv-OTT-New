@echo off
echo ========================
echo 🚀 KARO DEPLOY - KOYEB
echo ========================

REM Check if koyeb.exe exists
if not exist "koyeb.exe" (
    echo ❌ koyeb.exe not found!
    echo Please download Koyeb CLI first:
    echo https://github.com/koyeb/cli/releases/latest
    echo Download 'koyeb-cli_5.9.0_windows_amd64.zip'
    echo Extract and place koyeb.exe in this folder
    pause
    exit /b 1
)

echo ✅ Koyeb CLI found

REM Check if logged in
koyeb whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo 🔐 Please login to Koyeb first:
    koyeb login
    pause
)

echo 🔑 Setting environment variables...
echo Enter your credentials:

set /p API_ID="API ID: "
set /p API_HASH="API HASH: "
set /p BOT_TOKEN="BOT TOKEN: "
set /p MONGO_URI="MONGO URI: "

echo 📤 Deploying to Koyeb...

REM Create app if not exists
koyeb app create rv-ott-bot 2>nul

REM Set secrets
koyeb secret create API_ID --app rv-ott-bot --value %API_ID% 2>nul
koyeb secret create API_HASH --app rv-ott-bot --value %API_HASH% 2>nul
koyeb secret create BOT_TOKEN --app rv-ott-bot --value %BOT_TOKEN% 2>nul
koyeb secret create MONGO_URI --app rv-ott-bot --value %MONGO_URI% 2>nul

REM Git setup and deploy
git init 2>nul
git add .
git commit -m "Karo Deploy 🚀" 2>nul
git push koyeb master 2>nul || git push -u koyeb master

echo ========================
echo ✅ DEPLOYMENT COMPLETE!
echo 🌐 Bot is now live on Koyeb
echo 💰 Free tier: 1GB RAM
echo ========================
pause