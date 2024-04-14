from bot.utils.pydantic import Model
from typing import List, Dict


class Image(Model):
    url: str
    width: int
    height: int


class Artist(Model):
    id: str
    name: str
    picture: List[Image]
    main: bool


class Album(Model):
    id: str
    title: str
    imageCover: List[Image]
    videoCover: List


class Track(Model):
    artifactType: str
    id: str
    title: str
    artists: List[Artist]
    album: Album
    duration: int
    trackNumber: int
    volumeNumber: int
    isrc: str
    copyright: str
    mediaMetadata: Dict
    properties: Dict
    tidalUrl: str
