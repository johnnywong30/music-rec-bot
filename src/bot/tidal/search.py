from __future__ import annotations
from typing import TypedDict, Literal
from bot.tidal import API_URL, get_headers
from bot.tidal.auth import get_tidal_token
import httpx


class SearchQuery(TypedDict):
    query: str
    type: SEARCH_TYPES
    offset: int
    limit: int
    countryCode: str
    popularity: POPULARITY_TYPES


async def search_track(
    track_name: str,
    artist_name: str | None = None,
    offset: int = 0,
    limit: int = 10,
    country_code: str = "US",
    popularity: POPULARITY_TYPES = "WORLDWIDE",
):
    search_url = API_URL + "/search"
    params = SearchQuery(
        query=track_name,
        type="TRACKS",
        offset=offset,
        limit=limit,
        countryCode=country_code,
        popularity=popularity,
    )
    async with httpx.AsyncClient() as client:
        auth = await get_tidal_token()
        headers = get_headers(token=auth["access_token"])
        response = await client.get(
            url=search_url,
            params=params,
            headers=headers,
        )
        response = response.json()
    return response


SEARCH_TYPES = Literal["ARTISTS", "ALBUMS", "TRACKS", "VIDEOS"]
POPULARITY_TYPES = Literal["WORLDWIDE", "COUNTRY"]
