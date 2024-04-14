from bot.client import bot
from discord.ext.commands import Context
from bot.commands.tidal import *


@bot.command()
async def ping(context: Context):
    await context.send("pong")
