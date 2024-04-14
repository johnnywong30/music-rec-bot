from __future__ import annotations
from typing import TypedDict, Literal, List, Dict
from bot.tidal import API_URL, get_headers
from bot.tidal.auth import get_tidal_token
import httpx
from bot.tidal.models import Track
from bot.logging import log
import json


class SearchQuery(TypedDict):
    query: str
    type: SEARCH_TYPES
    offset: int
    limit: int
    countryCode: str
    popularity: POPULARITY_TYPES


def find_track_with_artist(tracks: List[Dict], artist_name: str) -> List[Dict]:
    tracks_with_artist = [
        track
        for track in tracks
        if len([artist for artist in track["artists"] if artist["name"] == artist_name])
        > 0
    ]
    return tracks_with_artist


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
        if artist_name:
            track_found = False
            while not track_found:
                response = await client.get(
                    url=search_url,
                    params=params,
                    headers=headers,
                )
                response_json = response.json()
                tracks = response_json["tracks"]
                tracks = [track["resource"] for track in tracks]
                tracks_with_artist = find_track_with_artist(tracks, artist_name)
                # return tracks_with_artist
                if len(tracks_with_artist) > 0:
                    track = Track(**tracks_with_artist[0])
                    return track
                else:
                    offset += limit
        else:
            response = await client.get(
                url=search_url,
                params=params,
                headers=headers,
            )
            response_json = json.loads(response.text)
            tracks = response_json["tracks"]
            tracks = [track["resource"] for track in tracks]
            track = Track(**tracks[0])

            return track


SEARCH_TYPES = Literal["ARTISTS", "ALBUMS", "TRACKS", "VIDEOS"]
POPULARITY_TYPES = Literal["WORLDWIDE", "COUNTRY"]
