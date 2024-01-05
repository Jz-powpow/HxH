#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 26032794, #get it from https://my.telegram.org/auth
    api_hash="1ccced9f1c971ee459e5c539792cb2f6", #get it from https://my.telegram.org/auth
    bot_token="6973378210:AAG9WARDLIVfvmRZ8QQ6tsJdyUCvcGtyO1s", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
