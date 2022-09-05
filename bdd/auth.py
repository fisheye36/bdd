import base64
import hashlib
import hmac
import urllib.parse
import time


def generate_nonce() -> int:
    return int(time.time() * 1000)


def generate_api_key_signature(uri: str, data: dict[str, str | int], secret: str) -> str:
    encoded_post_data = urllib.parse.urlencode(data)
    nonce_with_encoded_post_data = f'{data["nonce"]}{encoded_post_data}'.encode()

    message = uri.encode() + hashlib.sha256(nonce_with_encoded_post_data).digest()
    mac = hmac.new(
        key=base64.b64decode(secret),
        msg=message,
        digestmod=hashlib.sha512,
    )

    signature_digest = base64.b64encode(mac.digest())
    signature_digest_as_str = signature_digest.decode()

    return signature_digest_as_str
