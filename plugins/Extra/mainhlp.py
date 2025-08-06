"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from asgiref.sync import sync_to_async
from requests import get



@sync_to_async
def parse_spotify_url(url):
    if url.startswith("spotify"):
        return url.split(":")[1]
    url = get(url).url
    parsed_url = url.replace("https://open.spotify.com/", "").split("/")
    return parsed_url[0], parsed_url[1].split("?")[0]


@sync_to_async
def thumb_down(link, name):
    with open(f"/tmp/thumbnails/{name}.jpg", "wb") as file:
        if get(link).status_code == 200:
            file.write(get(link).content)
        else:
            file.write(
                get(
                    "https://telegra.ph/file/1ee248e6a6104faeee1b7.jpg"
                ).content
            )
    return f"/tmp/thumbnails/{name}.jpg"

@sync_to_async
def fetch_spotify_track(client, item_id):
    """
    Fetch tracks from provided item.
    """
    item = client.track(track_id=item_id)
    track_name = item.get("name")
    album_info = item.get("album")
    track_artist = ", ".join([artist["name"] for artist in item["artists"]])
    if album_info:
        track_album = album_info.get("name")
        track_year = (
            album_info.get("release_date")[:4]
            if album_info.get("release_date")
            else ""
        )
        album_total = album_info.get("total_tracks")
    track_num = item["track_number"]
    deezer_id = item_id
    cover = (
        item["album"]["images"][0]["url"]
        if len(item["album"]["images"]) > 0
        else None
    )
    genre = (
        client.artist(artist_id=item["artists"][0]["uri"])["genres"][0]
        if len(client.artist(artist_id=item["artists"][0]["uri"])["genres"])
        > 0
        else ""
    )
    offset = 0
    return {
        "name": track_name,
        "artist": track_artist,
        "album": track_album,
        "year": track_year,
        "num_tracks": album_total,
        "num": track_num,
        "playlist_num": offset + 1,
        "cover": cover,
        "genre": genre,
        "deezer_id": deezer_id,
    }


