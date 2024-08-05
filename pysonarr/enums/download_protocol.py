"""
Sonarr Download Protocol Enum.
"""

from enum import Enum


class DownloadProtocol(Enum):
    """
    Sonarr Download Protocol Enum
    """

    UNKNOWN = "unknown"
    USENET = "usenet"
    TORRENT = "torrent"
