import json
import urllib.request
import urllib.parse

from typing import Callable

from .exceptions import APIKeyError
from .config import BASE_URL


def validate_api_kay(api_key: str) -> bool:
    """Validate the API key format.
    Args:
        api_key (str): The API key to validate.
    Returns: 
        bool: True if the API key is valid, False otherwise.
    """
    return len(api_key) > 10 and api_key.isalnum()


def newsapi_client(api_key: str, query: str, timeout: int = 30, retries: int = 3):
    try:
        query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
        url = f"{BASE_URL}?{query_string}"
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read()
            return json.loads(data.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error fetching news: {e}, type: {type(e)}")
        raise APIKeyError("Invalid API key or request error.")
    

def guardian_client(api_key: str, section: str, from_date: str, timeout: int = 30, retries: int = 3):
    return f"Guardian {section} from {from_date} with timeout {timeout}"


def fetch_news(api_name: str, *args: tuple, **kwargs: dict) -> dict:
    """Function that receives the API name and parameters, and call to the corresponding client.
    Args:
        api_name (str): The name of the API to call."""

    if api_name not in ("newsapi", "guardian"):
        raise ValueError(f"Unsupported API: {api_name}")

    base_config = {
        "timeout": 30,
        "retries": 3
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients: dict[str, Callable] = {
        "newsapi": newsapi_client,
        "guardian": guardian_client
    }

    client: str = api_clients[api_name]
    return client(*args, **config)