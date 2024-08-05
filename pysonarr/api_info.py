"""
This module contains the API information for Sonarr.
"""

from pysonarr.client import SonarrClient


class ApiInfo:
    """
    Sonarr API information
    """

    def __init__(self, base_url, api_key):
        """
        Initialize the Sonarr API information
        """
        self.base_url = base_url
        self.api_key = api_key
        self.client = SonarrClient(base_url, api_key)

    def get_api_info(self):
        """
        Get the Sonarr API information
        """
        return self.client.get("/api")
