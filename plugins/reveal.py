from pyrogram.client import Client as app
from pyrogram.types import Message
from config import bot_id
from json import load

with open("utilities/reply/text/text.json", "r", encoding="utf-8") as file:
    text = load(file)

@app.on_message()
async def main(client:app, message:Message):
    if not message.text:
        return 
    
    if message.chat.id == bot_id:
        chat_id, url = message.text.split()
        poll_chat_id, poll_message_id = url.split("/")[-2:]

        getted_message = await client.get_messages(poll_chat_id, int(poll_message_id))

        if str(getted_message.poll.correct_option_id):
            correct_poll_id = getted_message.poll.correct_option_id
            correct_poll_text = getted_message.poll.options[correct_poll_id].text
            await message.reply(text["user_msg"].format(int(chat_id), correct_poll_text))
            return

        choosed_message = await getted_message.vote(0)
        correct_poll_id = choosed_message.correct_option_id
        correct_poll_text = choosed_message.options[correct_poll_id].text
        await message.reply(text["user_msg"].format(int(chat_id), correct_poll_text))
