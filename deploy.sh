#!/bin/bash

echo "🚀 Deploying RV OTT Bot to Heroku..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first."
    exit 1
fi

# Check if logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "❌ Not logged in to Heroku. Please run 'heroku login' first."
    exit 1
fi

# Create Heroku app if it doesn't exist
APP_NAME="rv-ott-bot"
echo "📦 Checking if app exists..."
if ! heroku apps:info $APP_NAME &> /dev/null; then
    echo "🆕 Creating new Heroku app..."
    heroku create $APP_NAME
else
    echo "✅ App already exists: $APP_NAME"
fi

# Set buildpacks
echo "⚙️ Setting buildpacks..."
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt

# Set environment variables (you'll need to set these manually)
echo "🔑 Please set the following environment variables:"
echo "heroku config:set API_ID=your_api_id"
echo "heroku config:set API_HASH=your_api_hash" 
echo "heroku config:set BOT_TOKEN=your_bot_token"
echo "heroku config:set MONGO_URI=your_mongo_uri"
echo "heroku config:set DATABASE_NAME=your_database_name"

# Deploy using git
echo "📤 Deploying code..."
git init
git add .
git commit -m "Initial deployment"
git push heroku master

echo "✅ Deployment complete!"
echo "🔧 Don't forget to scale your dynos:"
echo "heroku ps:scale worker=1"