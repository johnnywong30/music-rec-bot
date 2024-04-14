from typing import Dict

API_URL = "https://openapi.tidal.com"
_CONTENT_TYPE = "application/vnd.tidal.v1+json"


def get_headers(token: str, token_type: str = "Bearer") -> Dict[str, str]:
    auth = f"{token_type} {token}"
    return {
        "accept": _CONTENT_TYPE,
        "Authorization": auth,
        "Content-Type": _CONTENT_TYPE,
    }
