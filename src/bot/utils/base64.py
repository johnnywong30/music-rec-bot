import base64


def encode_base64(s: str) -> str:
    x = s.encode("ascii")
    b64 = base64.b64encode(x)
    encoded_str = b64.decode("ascii")
    return encoded_str
