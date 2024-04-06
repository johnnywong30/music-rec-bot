import logging
from bot.context import Config

_log_level = logging.DEBUG if Config.environment == "DEV" else logging.INFO

logging.basicConfig(
    level=_log_level,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
log = logging.getLogger(__name__)
