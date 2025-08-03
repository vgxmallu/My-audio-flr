import os
from pyrogram import Client, filters
import lyricsgenius
from pyrogram.types import Message, User
import requests
#from config import LOG_CHANNEL


#  Lyrics--------------------

ML = """
📣 **LOG ALERT** 📣

📛**Triggered Command** : /lyrics {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
"""

@Client.on_message(filters.command("lyrh"))
async def lrseharch(bot, message: Message):  
    m = await message.reply_text("Finding your Lyrics🎼...")
    query = message.text.split(None, 1)[1]
    x = "Aiiyg6QbQzs5eBqzXz3jRYcK4aPl5X1reag7WT8b6Rbb61t1cX57aYOTQL7DSdsm2ARnXAiYg_BbR5n1G3Uz4A"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not Found :(")
        
    xxx = f"""
🔎 **Searched Song:** __{query}__
🎶 **Found Lyrics For:** __{S.title}__
👨‍🎤 **Artist:** {S.artist}
💜 **Requested by:** {message.from_user.mention}

**Lyrics:**
`{S.lyrics}`

©️ **Lyrics Searched By @Musicx_dlbot**"""
    await m.edit(xxx)
    #await bot.send_message(LOG_CHANNEL, ML.format(query, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
