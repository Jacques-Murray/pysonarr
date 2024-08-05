"""
Sonarr Season Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.schemas.media_cover import MediaCover
from pysonarr.schemas.season_statistics_resource import SeasonStatisticsResource


@dataclass
class SeasonResource:
    """
    Sonarr Season Resource Schema
    """

    season_number: int
    monitored: bool
    statistics: Optional[SeasonStatisticsResource]
    images: Optional[List[MediaCover]]
