from bot.client import bot
from discord.ext.commands import Context
from bot.logging import log
import httpx
from bot.tidal.search import search_track


@bot.command()
async def song(context: Context, song: str, artist_name: str | None = None):
    log.info(f"{context.author} requested song details with args {context.args}")
    track = await search_track(song)
    log.info(track)