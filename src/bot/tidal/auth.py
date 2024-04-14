import httpx
from bot.context import Config
from bot.utils.base64 import encode_base64
from typing import TypedDict

_client_id = Config.tidal_id
_client_secret = Config.tidal_secret

_tidal_auth_url = "https://auth.tidal.com/v1/oauth2/token"


class TidalToken(TypedDict):
    access_token: str
    token_type: str
    expires_in: int


async def get_tidal_token() -> TidalToken:
    credentials = f"{_client_id}:{_client_secret}"
    encoded_credentials = encode_base64(credentials)
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Basic {encoded_credentials}"}
        data = {"grant_type": "client_credentials"}
        response = await client.post(_tidal_auth_url, headers=headers, data=data)
        response = response.json()
    token = TidalToken(
        access_token=response["access_token"],
        token_type=response["token_type"],
        expires_in=response["expires_in"],
    )
    return token
