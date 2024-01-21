from pyrogram import Client

async def link_checker(link, client:Client):
    try:
        message_id = link.split("/")[-1]
        chat_id = link.split("/")[-2]

        getted_message = await client.get_messages(chat_id, int(message_id))

        return getted_message
    
    except Exception as e:
        if str(e).strip() == "Client has not been started yet":
            return str(e).strip()

        else:
            print(e)
            return False
