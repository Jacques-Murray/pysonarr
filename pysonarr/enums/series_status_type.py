"""
Sonaar Series Status Type Enum
"""

from enum import Enum


class SeriesStatusType(Enum):
    """
    Sonarr Series Status Type Enum
    """

    CONTINUING = "continuing"
    ENDED = "ended"
    UPCOMING = "upcoming"
    DELETED = "deleted"
