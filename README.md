# RV-OTT-Bot

A Telegram bot for downloading DRM protected content with Widevine CDM support.

## Features
- Download DRM protected content from various platforms
- Widevine CDM integration for content decryption
- Google Drive upload support
- Multiple platform support (Hotstar, YouTube, etc.)
- Subscription-based access control

## Prerequisites
- Python 3.9+
- Telegram Bot Token
- Google Drive API credentials
- MongoDB database

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rv-ott-bot.git
cd rv-ott-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the bot:
```bash
python bot.py
```

## Configuration

Required environment variables:
- `API_ID` - Telegram API ID
- `API_HASH` - Telegram API Hash
- `BOT_TOKEN` - Telegram Bot Token
- `OWNER_ID` - Your Telegram User ID
- `DB_URL` - MongoDB connection URL

## Deployment

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Koyeb
Use the provided `koyeb.yml` configuration file.

## Usage

Send supported URLs to the bot to download content. Supported platforms include:
- Hotstar (DRM protected)
- YouTube
- And other platforms supported by yt-dlp

## License

This project is for educational purposes only. Use at your own risk.