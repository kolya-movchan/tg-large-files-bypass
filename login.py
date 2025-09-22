from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

client = TelegramClient("session", API_ID, API_HASH)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(PHONE_NUMBER)
    code = input("Enter the code you received: ")
    
    try:
        client.sign_in(PHONE_NUMBER, code)
    except SessionPasswordNeededError:
        # 2FA is enabled, need to enter password
        password = input("Enter your 2FA password: ")
        client.sign_in(password=password)


print("✅ Logged in and session saved.")
client.disconnect()
