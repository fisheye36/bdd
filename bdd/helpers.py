import auth
from config import settings


def get_uri_from_endpoint(endpoint: str) -> str:
    return endpoint.removeprefix(settings.base_url)


def build_post_headers(uri: str, form_data: dict[str, str | int]) -> dict[str, str]:
    headers = {
        'API-Key': settings.auth.api_key,
        'API-Sign': auth.generate_api_key_signature(
            uri=uri,
            data=form_data,
            secret=settings.auth.api_secret,
        ),
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return headers
