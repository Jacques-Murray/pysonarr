"""
Sonarr Privacy Level Enum
"""

from enum import Enum


class PrivacyLevel(Enum):
    """
    Sonarr Privacy Level Enum
    """

    NORMAL = "normal"
    PASSWORD = "password"
    API_KEY = "apiKey"
    USER_NAME = "userName"
