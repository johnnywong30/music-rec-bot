from bot.context import Config
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=Config.intents)
