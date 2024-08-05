"""
Sonarr Apply Tags Enum
"""

from enum import Enum


class ApplyTags(Enum):
    """
    Apply Tags Enum
    """

    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
