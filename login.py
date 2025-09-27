from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os

API_ID_VI = int(os.getenv("API_ID_VI"))
API_HASH_VI = os.getenv("API_HASH_VI")
PHONE_NUMBER_VI = os.getenv("PHONE_NUMBER_VI")

client = TelegramClient("session", API_ID_VI, API_HASH_VI)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(PHONE_NUMBER_VI)
    code = input("Enter the code you received: ")
    
    try:
        client.sign_in(PHONE_NUMBER_VI, code)
    except SessionPasswordNeededError:
        # 2FA is enabled, need to enter password
        password = input("Enter your 2FA password: ")
        client.sign_in(password=password)


print("✅ Logged in and session saved.")
client.disconnect()
