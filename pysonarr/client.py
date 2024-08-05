"""
Sonarr API client
"""

import requests
from requests.exceptions import HTTPError


class SonarrClient:
    """
    Sonarr API client
    """

    def __init__(self, base_url, api_key):
        """
        Initialize the Sonarr API client
        """
        self.base_url = base_url
        self.api_key = api_key

    def _request(self, method, path, **kwargs):
        """
        Make a request to the Sonarr API
        """
        url = f"{self.base_url}{path}"
        headers = {"X-Api-Key": self.api_key}

        try:
            response = requests.request(
                method, url, headers=headers, timeout=10, **kwargs
            )
            response.raise_for_status()
        except HTTPError as e:
            raise e

        return response.json()

    def get(self, path, **kwargs):
        """
        Make a GET request to the Sonarr API
        """
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        """
        Make a POST request to the Sonarr API
        """
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        """
        Make a PUT request to the Sonarr API
        """
        return self._request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        """
        Make a DELETE request to the Sonarr API
        """
        return self._request("DELETE", path, **kwargs)
