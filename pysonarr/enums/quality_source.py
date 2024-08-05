"""
Sonarr Quality Source Enum
"""

from enum import Enum


class QualitySource(Enum):
    """
    Sonarr Quality Source Enum
    """

    UNKNOWN = "unknown"
    TELEVISION = "television"
    TELEVISION_RAW = "televisionRaw"
    WEB = "web"
    WEB_RIP = "webRip"
    DVD = "dvd"
    BLURAY = "bluray"
    BLURAY_RAW = "blurayRaw"
