#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
TO_CHANNEL = config("TO_CHANNEL")  # Replace this with the username or chat ID of your destination channel

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(outgoing=True))
async def forward_to_channel(event):
    if event.is_channel and event.chat.username == "@AKFilte1bot":  # Replace 'your_bot_username' with your bot's username
        try:
            await BotzHubUser.send_message(
                TO_CHANNEL,
                event.message
            )
            print(f"Message forwarded from bot chat to {TO_CHANNEL}")
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
