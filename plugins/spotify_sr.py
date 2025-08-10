from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy
from pyrogram import filters, Client 

from plugins.Extra.mainhlp import (
    fetch_spotify_track,
    parse_spotify_url,
    thumb_down,
)


SPOTIPY_CLIENT_ID = "9bc099cf511348748c885636a99e8214"
SPOTIPY_CLIENT_SECRET = "1a49370594b543ba915a7bb8f55ec68d"

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#client = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials())




@Client.on_message(filters.incoming & filters.regex(r'https?://open.spotify.com[^\s]+') | filters.incoming & filters.regex(r'https?://spotify.link[^\s]+'), group=-2)
async def spotifyvx(bot, message):
    link = message.matches[0].group(0)
    m = await message.reply_text(f"**Gathering info from your [link]({link}).**")
    try:
        parsed_item = await parse_spotify_url(link)
        item_type, item_id = parsed_item[0], parsed_item[1]
        randomdir = f"/tmp/{str(randint(1,100000000))}"
        mkdir(randomdir)
        if item_type in "track":
            song = await fetch_spotify_track(client, item_id)
            await message.reply_photo(
                song.get("cover"),
                caption=f"🧾Track Details:\n\n🎧 Title: {song['name']}\n👤 Artist: {song['artist']}\n💽 Album: {song['album']}\n📅 Date: {song['year']}\n⛓️‍💥 Link: {link}",
            )
            await m.delete()
    except Exception as e:
    print("An error occurred:", e)
