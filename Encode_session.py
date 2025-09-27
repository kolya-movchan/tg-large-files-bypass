from telethon.sync import TelegramClient
import os
import base64

# Function to encode session file to base64 string
def encode_session_to_base64(session_file_path="session.session"):
    try:
        with open(session_file_path, "rb") as f:
            session_data = f.read()
        
        # Encode to base64
        session_b64 = base64.b64encode(session_data).decode('utf-8')
        
        # Save to a text file
        with open("session_encoded.txt", "w") as f:
            f.write(session_b64)
        
        print(f"✅ Session encoded successfully!")
        print(f"📁 Encoded session saved to: session_encoded.txt")
        print(f"📝 Base64 string length: {len(session_b64)} characters")
        print(f"🔗 First 100 characters: {session_b64[:100]}...")
        
        return session_b64
        
    except FileNotFoundError:
        print("❌ Error: session.session file not found!")
        print("Make sure you've run login.py first to create the session file.")
        return None
    except Exception as e:
        print(f"❌ Error encoding session: {e}")
        return None

# Encode the session
encoded_session = encode_session_to_base64()

# Optionally, you can also set it as an environment variable for later use
if encoded_session:
    print(f"\n💡 To use this encoded session later, set environment variable:")
    print(f"export SESSION_B64=\"{encoded_session}\"")

# Rest of your existing code (decode and read messages)
session_b64 = os.getenv("SESSION_B64")
if session_b64:
    session_data = base64.b64decode(session_b64)
    with open("session.session", "wb") as f:
        f.write(session_data)
    session_name = "session"
else:
    session_name = "session"  # Assuming you already have session.session locally

# Set your API credentials
API_ID_VI = int(os.getenv("API_ID_VI"))
API_HASH_VI = os.getenv("API_HASH_VI")

# Who you want to read messages from
chat_username = "@video_auto_upload_vi_bot"  # Replace this with the bot's username

with TelegramClient(session_name, API_ID_VI, API_HASH_VI) as client:
    messages = client.get_messages(chat_username, limit=10)
    for msg in messages:
        print(f"ID: {msg.id}")
        print(f"Text: {msg.text}")
        print(f"Has media: {'✅' if msg.media else '❌'}")
        print("-----")
