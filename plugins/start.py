from pyrogram.client import Client as app
from pyrogram import filters
from utilities.reply import button 
from utilities.database import Database
from json import load

with open("utilities/reply/text/text.json", "r", encoding="utf-8") as file:
    text = load(file)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    chat_id = message.chat.id

    if not Database.find_user(chat_id):
        Database.add_user(chat_id)
    
    first_name = message.from_user.first_name
    await message.reply(text["start"].format(first_name), reply_markup=button.start)
