from __future__ import annotations
import httpx
from typing import TypedDict, List
from bot.tidal import API_URL, get_headers
from bot.tidal.auth import get_tidal_token
from bot.tidal.models import Track


class TrackQuery(TypedDict):
    offset: int
    limit: int
    countryCode: str


class _Track(TypedDict):
    id: str


class SimilarTrack(TypedDict):
    resource: _Track


async def get_similar_tracks(
    trackId: str,
    country_code: str = "US",
    offset: int = 0,
    limit: int = 10,
):
    url = f"{API_URL}/tracks/{trackId}/similar"
    async with httpx.AsyncClient() as client:
        auth = await get_tidal_token()
        headers = get_headers(token=auth["access_token"])
        params = TrackQuery(offset=offset, limit=limit, countryCode=country_code)
        response = await client.get(url=url, headers=headers, params=params)
        data: List[SimilarTrack] = response.json()["data"]
    return data


async def get_track(trackId: str, country_code: str = "US") -> Track:
    url = f"{API_URL}/tracks/{trackId}"
    async with httpx.AsyncClient() as client:
        auth = await get_tidal_token()
        headers = get_headers(token=auth["access_token"])
        params = {"countryCode": country_code}
        response = await client.get(url=url, headers=headers, params=params)
        track = Track(**response.json()["resource"])
    return track
