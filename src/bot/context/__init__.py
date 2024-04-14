from dotenv import load_dotenv
import os
from discord import Intents
from typing import Literal

load_dotenv()

ENVIRONMENTS = Literal["DEV", "PROD"]


def _discord_intents():
    intents = Intents.default()
    intents.message_content = True
    return intents


class Config:
    discord_token = os.environ["DISCORD_TOKEN"]
    intents = _discord_intents()
    environment: ENVIRONMENTS = os.environ["ENVIRONMENT"]
    tidal_id = os.environ["TIDAL_CLIENT_ID"]
    tidal_secret = os.environ["TIDAL_CLIENT_SECRET"]
