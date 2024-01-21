from config import bot_token, api_id, api_hash, session_string
from pyrogram.client import Client
import pyrogram

bot_plugins = ["broadcast", "start", "result", "poll"]
user_plugins =["reveal"]
bot = Client("Bot", bot_token=bot_token, api_id=api_id, api_hash=api_hash, plugins={"root":"plugins", "include":bot_plugins})
user = Client("User", session_string=session_string, api_id=api_id, api_hash=api_hash, plugins={"root":"plugins", "include":user_plugins})

if __name__== "__main__":
    pyrogram.compose([user, bot])
