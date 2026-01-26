#!/bin/bash

echo "🚀 Deploying RV OTT Bot to Koyeb..."

# Check if Koyeb CLI is installed
if ! command -v koyeb &> /dev/null; then
    echo "❌ Koyeb CLI not found. Installing..."
    curl -sSL https://raw.githubusercontent.com/koyeb/cli/master/install.sh | sh
fi

# Check if logged in to Koyeb
if ! koyeb whoami &> /dev/null; then
    echo "❌ Not logged in to Koyeb. Please run 'koyeb login' first."
    koyeb login
fi

# Create app
echo "🆕 Creating Koyeb app..."
koyeb app create rv-ott-bot

# Set environment variables
echo "🔑 Setting environment variables..."
echo "Please enter your credentials:"

read -p "API ID: " API_ID
read -p "API HASH: " API_HASH  
read -p "BOT TOKEN: " BOT_TOKEN
read -p "MONGO URI: " MONGO_URI

koyeb secret create API_ID --app rv-ott-bot --value "$API_ID"
koyeb secret create API_HASH --app rv-ott-bot --value "$API_HASH"
koyeb secret create BOT_TOKEN --app rv-ott-bot --value "$BOT_TOKEN"
koyeb secret create MONGO_URI --app rv-ott-bot --value "$MONGO_URI"

# Deploy using git
echo "📤 Deploying code..."
git init
git add .
git commit -m "Initial Koyeb deployment"
git push koyeb master

echo "✅ Deployment complete!"
echo "🌐 Your bot is now running on Koyeb!"
echo "💰 Free tier includes 1GB RAM and 512MB storage"