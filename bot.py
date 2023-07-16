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
import time
from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_CHANNEL = config("FROM_CHANNEL", default=None)
TO_CHANNEL = config("TO_CHANNEL", default=None)

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

async def forward_existing_videos(source_channel, target_channel):
    async for message in BotzHubUser.iter_messages(source_channel):
        if message.media and message.media.document and message.media.document.mime_type.startswith('video'):
            try:
                await BotzHubUser.forward_messages(target_channel, message)
                print(f"Video forwarded from {source_channel} to {target_channel}")
            except Exception as e:
                print(e)

print("Bot has started.")

# Add your source channel or chat ID here
if FROM_CHANNEL and TO_CHANNEL:
    BotzHubUser.loop.run_until_complete(forward_existing_videos(FROM_CHANNEL, TO_CHANNEL))

BotzHubUser.run_until_disconnected()
