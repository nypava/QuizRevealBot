# Quiz Reveal Bot
Using this bot, you can get the answer of any valid public polls

## 💫 Features
- Gives any public quiz mode poll answers
- Instant 

## 🗃️ Installation & Setup
```
git clone https://github.com/NYDEV0/QuizRevealBot
cd QuizRevealBot
pip install -r requirements.txt
```
In config.py file configure with your own data.

```
api_id = "" # Telegram api id from https://my.telegram.org 
api_hash = "" # Telegram api hash from https://my.telegram.org 
owner_id = 000000 # Telegram bot owner id. You can get it by sending /id your_username command to @MissRose_bot. Example /id @username
user_id = 00000 # Telegram account user id, which used to get poll answer.      
bot_id = 00000 # Telegram bot id. You can get it by sending /id your_username command to @MissRose_bot. Example /id @username 
session_string = "" # Pyrogram Telegram session string which used to gain access in the user account and get poll answer. You can generate using https://github.com/GojouSats/Pyrostring 
bot_token = "" # Telegram bot token from @BotFather 
mongo_token = "" # Mongo key from https://www.mongodb.com/atlas/database, Want tutorial on ""how to get mongod_key"? Here is one - https://youtu.be/0Pt7Kfh78Jg?si=LAFwfyMATmQ3SRST 
```
## ⚙️  Usage
User and Admin
- Copy message url of the poll and send it to the bot, it will reply to you with the answer.

Admin only
- Reply to your message with /broadcast command to broadcast to all users that started the bot.
