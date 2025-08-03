import os
from pyrogram import Client as app, filters
import requests

# Replace these with your own credentials or set them as environment variables

LYRICS_API_URL = "https://api.lyrics.ovh/v1/{artist}/{title}"

def get_lyrics(artist, title):
    url = LYRICS_API_URL.format(artist=artist, title=title)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data.get("lyrics", "Lyrics not found.")
    else:
        return "Lyrics not found. Try another song!"



@app.on_message(filters.command("lyr4"))
async def lyrics4(_, message):
    if " - " not in message.text:
        await message.reply("Send the song name in `Artist - Title` format, e.g. /lyr4 `Adele - Hello`")
        return
    #query = message.text.split(None, 1)[1]
    artist, title = message.text.split(" - ", 1)
    await message.reply("Searching lyrics...")

    lyrics = get_lyrics(artist.strip(), title.strip())
    # Avoid sending overly long messages
    if len(lyrics) > 4096:
        await message.reply("Lyrics are too long to send in one message. Here's the first part:\n\n" + lyrics[:4000])
    else:
        await message.reply(f"**{artist.strip()} - {title.strip()}**\n\n{lyrics}")

