import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from rvdb import Database
import asyncio
from flask import Flask
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
app = Client(
    "rvott_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# Initialize database
db = Database()

# Health check server for Koyeb
health_app = Flask(__name__)

@health_app.route('/')
def health_check():
    return {'status': 'ok', 'service': 'rv-ott-bot'}

@health_app.route('/health')
def health_status():
    return {'status': 'healthy', 'timestamp': str(asyncio.get_event_loop().time())}

# Start health check server in background
def start_health_server():
    health_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))

health_thread = threading.Thread(target=start_health_server, daemon=True)
health_thread.start()

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    await message.reply_text(
        "🎬 Welcome to RV OTT Bot!\n\n"
        "Send me a valid OTT platform link and I'll help you download it.\n"
        "Supported platforms: Hotstar, SonyLIV, Netflix, Amazon Prime, etc.\n\n"
        "⚠️ Note: This bot is for educational purposes only."
    )

@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    """Handle /help command"""
    await message.reply_text(
        "🤖 **Bot Commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/stats - Show download statistics\n\n"
        "📥 **How to use:**\n"
        "Simply send a valid OTT content link and the bot will process it.\n\n"
        "🔒 **Privacy:** Your links are processed securely and not stored."
    )

@app.on_message(filters.text & ~filters.command(["start", "help", "stats"]))
async def process_link(client: Client, message: Message):
    """Process OTT platform links"""
    user_id = message.from_user.id
    link = message.text.strip()
    
    # Check if link is valid
    if not is_valid_ott_link(link):
        await message.reply_text("❌ Invalid link format. Please send a valid OTT platform link.")
        return
    
    # Check user limits
    if not await db.can_download(user_id):
        await message.reply_text("❌ You've reached your daily download limit.")
        return
    
    # Process the download
    processing_msg = await message.reply_text("⏳ Processing your request...")
    
    try:
        # Here you would integrate with your actual download logic
        # This is a placeholder implementation
        result = await download_content(link, user_id)
        
        if result["success"]:
            await processing_msg.edit_text(
                f"✅ Download completed successfully!\n"
                f"📁 File: {result['filename']}\n"
                f"📊 Size: {result['size']}"
            )
            # Update user stats
            await db.increment_download_count(user_id)
        else:
            await processing_msg.edit_text(f"❌ Download failed: {result['error']}")
            
    except Exception as e:
        logger.error(f"Error processing download: {e}")
        await processing_msg.edit_text("❌ An error occurred while processing your request.")

def is_valid_ott_link(link: str) -> bool:
    """Check if the link is from a supported OTT platform"""
    supported_domains = [
        "hotstar.com",
        "sonyliv.com", 
        "netflix.com",
        "primevideo.com",
        "disneyplus.com",
        "mxplayer.in",
        "jiosaavn.com",
        "gaana.com"
    ]
    
    return any(domain in link.lower() for domain in supported_domains)

async def download_content(link: str, user_id: int) -> dict:
    """Placeholder for actual download implementation"""
    # This would integrate with your existing download logic
    # For now, returning mock data
    await asyncio.sleep(2)  # Simulate processing time
    
    return {
        "success": True,
        "filename": "sample_video.mp4",
        "size": "1.2 GB"
    }

@app.on_message(filters.command("stats"))
async def stats_command(client: Client, message: Message):
    """Show user statistics"""
    user_id = message.from_user.id
    stats = await db.get_user_stats(user_id)
    
    await message.reply_text(
        f"📊 **Your Statistics:**\n"
        f"Downloads today: {stats['downloads_today']}/{Config.DAILY_LIMIT}\n"
        f"Total downloads: {stats['total_downloads']}"
    )

if __name__ == "__main__":
    logger.info("Starting RV OTT Bot...")
    app.run()