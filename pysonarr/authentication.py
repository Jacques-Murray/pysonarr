"""
This module contains the authentication class for Sonarr.
"""

from pysonarr.client import SonarrClient


class Authentication:
    """
    Sonarr authentication
    """

    def __init__(self, base_url, api_key):
        """
        Initialize the Sonarr authentication
        """
        self.base_url = base_url
        self.api_key = api_key
        self.client = SonarrClient(base_url, api_key)

    def login(
        self,
        username: str = None,
        password: str = None,
        remember_me: str = None,
        return_url: str = None,
    ):
        """
        Login to Sonarr
        """
        return self.client.post(
            "/login",
            kwargs={"returnUrl": return_url},
            json={
                "username": username,
                "password": password,
                "rememberMe": remember_me,
            },
        )

    def logout(self):
        """
        Logout from Sonarr
        """
        return self.client.post("/logout")
