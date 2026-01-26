# RV OTT Bot

A Telegram bot for downloading content from various OTT platforms.

## Features
- Download from Hotstar, SonyLIV, Netflix, Amazon Prime, Disney+, MX Player, JioSaavn, Gaana
- Daily download limits per user
- MongoDB database for user statistics
- Docker support for easy deployment
- Heroku ready

## Prerequisites
- Python 3.8+
- Telegram Bot Token (from @BotFather)
- Telegram API ID and Hash (from https://my.telegram.org)
- MongoDB Atlas account (free tier available)

## Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Rv-OTT-New
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export API_ID=your_api_id
export API_HASH=your_api_hash
export BOT_TOKEN=your_bot_token
export MONGO_URI=your_mongodb_uri
export DATABASE_NAME=rvott_db
```

4. Run the bot:
```bash
python bot.py
```

## Koyeb Deployment (Recommended - Easier)

### Method 1: Using Deployment Script (Windows)
```cmd
 deploy-koyeb.bat
```

### Method 2: Manual Deployment
1. Install Koyeb CLI:
```bash
curl -sSL https://raw.githubusercontent.com/koyeb/cli/master/install.sh | sh
```

2. Login to Koyeb:
```bash
koyeb login
```

3. Create app:
```bash
koyeb app create rv-ott-bot
```

4. Set environment variables:
```bash
koyeb secret create API_ID --app rv-ott-bot --value your_api_id
koyeb secret create API_HASH --app rv-ott-bot --value your_api_hash
koyeb secret create BOT_TOKEN --app rv-ott-bot --value your_bot_token
koyeb secret create MONGO_URI --app rv-ott-bot --value your_mongo_uri
```

5. Deploy:
```bash
git init
git add .
git commit -m "Initial deployment"
git push koyeb master
```

## Heroku Deployment

### Method 1: Using Deployment Script (Windows)
```cmd
deploy.bat
```

### Method 2: Manual Deployment
1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create app:
```bash
heroku create your-app-name
```

4. Set buildpacks:
```bash
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku-community/apt
```

5. Set environment variables:
```bash
heroku config:set API_ID=your_api_id
heroku config:set API_HASH=your_api_hash
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set MONGO_URI=your_mongo_uri
heroku config:set DATABASE_NAME=your_database_name
```

6. Deploy:
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku master
```

7. Scale dynos:
```bash
heroku ps:scale worker=1
```

**Benefits of Koyeb:**
- Free tier with 1GB RAM
- No credit card required
- Automatic HTTPS
- Built-in monitoring
- Easier setup than Heroku

---

## Docker Deployment

1. Build the image:
```bash
docker build -t rvott-bot .
```

2. Run with environment variables:
```bash
docker run -e API_ID=your_api_id -e API_HASH=your_api_hash -e BOT_TOKEN=your_bot_token -e MONGO_URI=your_mongo_uri -e DATABASE_NAME=your_database_name rvott-bot
```

## Commands
- `/start` - Start the bot
- `/help` - Show help message
- `/stats` - Show download statistics

## Supported Platforms
- Hotstar
- SonyLIV
- Netflix
- Amazon Prime Video
- Disney+
- MX Player
- JioSaavn
- Gaana

## Configuration
Edit `config.py` to adjust settings like daily limits, database configuration, etc.

## License
This project is for educational purposes only. Use responsibly and respect copyright laws.# Rv-OTT-New
