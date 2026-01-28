#!/bin/bash

# Install any additional dependencies if needed
apt-get update && apt-get install -y ffmpeg git

# Set up environment
export PYTHONPATH="${PYTHONPATH}:/app"

# Start the bot
exec python bot.py