
import os
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("thumbdl"))
async def any_thumbnail(bot, m):
    try:
      query = m.text.split(None, 1)[1]
    except IndexError:
      await m.reply_text("__Give me some input the link..\ne.g: /thumbdl [Spotify-link or Deezer-link or YouTube-link]__")
      return
    mg = await m.reply_text("__Downloading your thumbnail, please wait...__")
    await asyncio.sleep(5)
    await m.reply_photo(f"{query}")
    await m.reply_text("Done ✅")
    await mg.delete()
