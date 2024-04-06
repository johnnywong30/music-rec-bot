from bot.logging import handler
from bot.commands import bot
from bot.context import Config

bot.run(token=Config.discord_token, log_handler=handler)
