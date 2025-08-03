import os
from pyrogram import Client as app, filters
import requests


# Genius API credentials (get your token from https://genius.com/developers)
GENIUS_TOKEN = os.environ.get("oT46akxcwAOxaOyktzPD2wuJW2HWHWJ2_sA72cqubBcbHXtXgh8SK5FkrLihH4Nq")
GENIUS_API_URL = "https://api.genius.com/search"


def search_genius(song_query):
    headers = {
        "Authorization": f"Bearer {GENIUS_TOKEN}"
    }
    params = {
        "q": song_query
    }
    resp = requests.get(GENIUS_API_URL, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    hits = data.get("response", {}).get("hits", [])
    if not hits:
        return None, None
    song_info = hits[0]["result"]
    title = song_info["title"]
    artist = song_info["primary_artist"]["name"]
    url = song_info["url"]
    return f"{artist} - {title}", url

def scrape_lyrics(url):
    import re
    from bs4 import BeautifulSoup
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return "Could not fetch lyrics from Genius."
    soup = BeautifulSoup(resp.text, "html.parser")
    lyrics_divs = soup.find_all("div", {"data-lyrics-container": "true"})t
    lyrics = "\n".join(div.get_text(separator="\n") for div in lyrics_divs)
    if not lyrics:
        match = re.search(r'<div\s+data-lyrics-container="true".*?>(.*?)</div>', resp.text, re.DOTALL)
        if match:
            lyrics = BeautifulSoup(match.group(1), "html.parser").get_text(separator="\n")
    return lyrics.strip() if lyrics else "Lyrics not found on Genius."


@app.on_message(filters.command("lyrica"))
async def lyrics_commandg(_, message):
    if len(message.command) < 2:
        await message.reply("Usage: `/lyrics <song name or artist - title>`\nExample: `/lyrics Alan Walker Alone`")
        return
    query = " ".join(message.command[1:]).strip()
    await message.reply("Searching Genius for lyrics...")
    song_title, song_url = search_genius(query)
    if not song_url:
        await message.reply("Couldn't find the song on Genius. Try another one!")
        return
    lyrics = scrape_lyrics(song_url)
    if len(lyrics) > 4096:
        await message.reply(
            f"**{song_title}**\n\nLyrics are too long to send in one message. Here's the first part:\n\n{lyrics[:4000]}"
        )
    else:
        await message.reply(f"**{song_title}**\n\n{lyrics}")

