@echo off
echo 🚀 Deploying RV OTT Bot to Heroku...

REM Check if Heroku CLI is installed
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Heroku CLI not found. Please install it first.
    pause
    exit /b 1
)

REM Check if logged in to Heroku
heroku auth:whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Not logged in to Heroku. Please run 'heroku login' first.
    pause
    exit /b 1
)

REM Set app name
set APP_NAME=rv-ott-bot

REM Check if app exists
heroku apps:info %APP_NAME% >nul 2>&1
if %errorlevel% neq 0 (
    echo 🆕 Creating new Heroku app...
    heroku create %APP_NAME%
) else (
    echo ✅ App already exists: %APP_NAME%
)

REM Set buildpacks
echo ⚙️ Setting buildpacks...
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt

REM Instructions for environment variables
echo.
echo 🔑 Please set the following environment variables:
echo heroku config:set API_ID=your_api_id
echo heroku config:set API_HASH=your_api_hash
echo heroku config:set BOT_TOKEN=your_bot_token
echo heroku config:set MONGO_URI=your_mongo_uri
echo heroku config:set DATABASE_NAME=your_database_name
echo.

REM Initialize git and deploy
echo 📤 Deploying code...
git init
git add .
git commit -m "Initial deployment"
git push heroku master

echo.
echo ✅ Deployment complete!
echo 🔧 Don't forget to scale your dynos:
echo heroku ps:scale worker=1
pause