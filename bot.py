#  @MrMNTG @MusammilN
#please give credits https://github.com/MN-BOTS/ShobanaFilterBot
import logging
import logging.config
import os
import sys
import asyncio
from datetime import date, datetime
import pytz
import aiohttp

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.CRITICAL - 1)

import tgcrypto
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, LOG_CHANNEL, KEEP_ALIVE_URL, DEFAULT_AUTH_CHANNELS
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script
from os import environ
from aiohttp import web as webserver
from telethon import TelegramClient, events, functions, types

# Peer ID invalid fix
from pyrogram import utils as pyroutils
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

from plugins.webcode import bot_run

PORT_CODE = environ.get("PORT", "8080")


formatter = logging.Formatter('%(levelname)s %(asctime)s - %(name)s - %(message)s')
fh = logging.FileHandler(f'{__name__}.log', 'w')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

telethon_logger = logging.getLogger("telethon")
telethon_logger.setLevel(logging.WARNING)
telethon_logger.addHandler(ch)
telethon_logger.addHandler(fh)
tbot = TelegramClient(__name__, API_ID, API_HASH, base_logger=telethon_logger).start(bot_token=BOT_TOKEN)
logger.info("TELETHON BOT STARTED...")


# ✅ Add this block
async def preload_auth_channels():
    if not await db.get_auth_channels():
        await db.set_auth_channels(DEFAULT_AUTH_CHANNELS)
        logging.info("Set default AUTH_CHANNELs in DB.")

async def keep_alive():
    """Send a request every 111 seconds to keep the bot alive (if required)."""
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Sent keep-alive request.")
            except Exception as e:
                logging.error(f"Keep-alive request failed: {e}")
            await asyncio.sleep(111)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def kulasthree(self):
        while True:
            await asyncio.sleep(24 * 60 * 60)
            logging.info("🔄 Bot is restarting")
            await self.send_message(chat_id=LOG_CHANNEL, text="🔄 Bot is restarting ...")
            os.execl(sys.executable, sys.executable, *sys.argv)

    async def start(self, **kwargs):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username

        # ✅ preload auth channels from info.py if DB is empty
        await preload_auth_channels()

        logging.info(f"{me.first_name} running on Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT)

        print("mntg4u</>")

        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_GC_TXT.format(today, time))

        asyncio.create_task(self.kulasthree())
        asyncio.create_task(keep_alive())

        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address, PORT_CODE).start()

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                yield message
                current += 1


app = Bot()
app.run()
