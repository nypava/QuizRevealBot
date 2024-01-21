from pyrogram.client import Client as app
from main import user
from pyrogram import enums, filters
from pyrogram.types import Message
from utilities.helpers.link_filter import link_filter
from utilities.helpers.link_checker import link_checker
from config import user_id
from json import load

with open("utilities/reply/text/text.json", "r", encoding="utf-8") as file:
    text = load(file)

@app.on_message(filters.private)
async def message_handler(client:app, message:Message):
    message_text = message.text if  message.text else ""
    chat_id = message.chat.id
    if link_filter(message_text):
        link_check:Message = await link_checker(message_text, user)

        if link_check == "Client has not been started yet":
            await user.start()
            link_check:Message = await link_checker(message_text, user)
        
        if link_check:
            if link_check.poll:
                if link_check.poll.type == enums.PollType.QUIZ:
                    await client.send_message(user_id, text["user_msg"].format(chat_id, message_text))
                    
                else:
                    await message.reply(text["wrong_poll"])

            else:
                await message.reply(text["wrong_type"])

        else:
            await message.reply(text["wrong_link"])

    else:
        await message.reply(text["wrong_message"])
