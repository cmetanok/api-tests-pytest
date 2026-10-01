import requests


class APIClient:
    """Тонкая обёртка над requests.Session для JSONPlaceholder API."""

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.post(f"{self.base_url}{endpoint}", **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.put(f"{self.base_url}{endpoint}", **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.patch(f"{self.base_url}{endpoint}", **kwargs)

    def close(self):
        self.session.close()