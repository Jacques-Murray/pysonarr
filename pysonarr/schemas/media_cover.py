"""
Sonarr Media Cover Schema
"""

from dataclasses import dataclass
from typing import Optional

from pysonarr.enums.media_cover_types import MediaCoverTypes


@dataclass
class MediaCover:
    """
    Sonarr Media Cover Schema
    """

    cover_type: MediaCoverTypes
    url: Optional[str]
    remote_url: Optional[str]
