from pyrogram.client import Client as app
from pyrogram import filters
from pyrogram.types import Message
from config import user_id
from json import load

with open("utilities/reply/text/text.json", "r", encoding="utf-8") as file:
    text = load(file)

@app.on_message(filters.user(user_id))
async def result(client:app, message:Message):
    chat_id = message.text.split()[0]
    answer = " ".join(message.text.split()[1:])
    await client.send_message(chat_id, text["correct_poll"].format(answer))
