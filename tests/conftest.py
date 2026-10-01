import pytest

from utils.api_client import APIClient


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def api(base_url: str):
    client = APIClient(base_url=base_url)
    yield client
    client.close()
