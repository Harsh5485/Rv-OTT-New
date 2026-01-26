@echo off
echo 🚀 Deploying RV OTT Bot to Koyeb...

REM Check if Koyeb CLI is installed
koyeb --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Koyeb CLI not found. Installing...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; irm get.scoop.sh | iex; scoop bucket add extras; scoop install koyeb" || curl -sSL https://raw.githubusercontent.com/koyeb/cli/main/install.sh | sh
)

REM Check if logged in to Koyeb
koyeb whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Not logged in to Koyeb. Please run 'koyeb login' first.
    echo Opening browser for login...
    koyeb login
    pause
)

REM Create app
echo 🆕 Creating Koyeb app...
koyeb app create rv-ott-bot

REM Set environment variables
echo 🔑 Setting environment variables...
echo Please enter your credentials:

set /p API_ID="API ID: "
set /p API_HASH="API HASH: "
set /p BOT_TOKEN="BOT TOKEN: "
set /p MONGO_URI="MONGO URI: "

koyeb secret create API_ID --app rv-ott-bot --value %API_ID%
koyeb secret create API_HASH --app rv-ott-bot --value %API_HASH%
koyeb secret create BOT_TOKEN --app rv-ott-bot --value %BOT_TOKEN%
koyeb secret create MONGO_URI --app rv-ott-bot --value %MONGO_URI%

REM Deploy using git
echo 📤 Deploying code...
git init
git add .
git commit -m "Initial Koyeb deployment"
git push koyeb master

echo ✅ Deployment complete!
echo 🌐 Your bot is now running on Koyeb!
echo 💰 Free tier includes 1GB RAM and 512MB storage
pause