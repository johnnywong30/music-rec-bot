from bot.client import bot
from discord.ext.commands import Context
from bot.logging import log
from bot.tidal.search import search_track
from bot.views import RecommendBtn


@bot.command()
async def song(context: Context, song: str, artist_name: str | None = None):
    log.info(
        f"{context.author} requested song details with args song={song}, artist_name={artist_name}"
    )
    try:
        track = await search_track(song, artist_name)
        song_template = "Title: {title}\nArtist: {artist}\nTidal URL: {url}"
        song_message = song_template.format(
            title=track.title,
            artist=", ".join([artist.name for artist in track.artists]),
            url=track.tidalUrl,
        )
        await context.send(song_message, view=RecommendBtn())
    except Exception as e:
        log.error(e)
        log.error(
            f"Failed to search track with arguments song={song}, artist_name={artist_name}"
        )
        await context.send(
            "Sorry, Tidal might have errored me out! Please try again or with a different song/artist combination!"
        )
