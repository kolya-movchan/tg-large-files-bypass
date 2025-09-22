from telethon.sync import TelegramClient
import os
import base64

# Decode your session from base64 (if stored in environment variable)
session_b64 = os.getenv("SESSION_B64")
if session_b64:
    session_data = base64.b64decode(session_b64)
    with open("session.session", "wb") as f:
        f.write(session_data)
    session_name = "session"
else:
    session_name = "session"  # Assuming you already have session.session locally

# Set your API credentials
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Who you want to read messages from
chat_username = "@video_auto_upload_vi_bot"  # Replace this with the bot's username

with TelegramClient(session_name, api_id, api_hash) as client:
    messages = client.get_messages(chat_username, limit=10)
    for msg in messages:
        print(f"ID: {msg.id}")
        print(f"Text: {msg.text}")
        print(f"Has media: {'✅' if msg.media else '❌'}")
        print("-----")
