"""
Sonarr Blocklist Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.enums.download_protocol import DownloadProtocol
from pysonarr.schemas.custom_format_resource import CustomFormatResource
from pysonarr.schemas.language import Language
from pysonarr.schemas.quality_model import QualityModel
from pysonarr.schemas.series_resource import SeriesResource


@dataclass
class BlocklistResource:
    """
    Sonarr Blocklist Resource Schema
    """

    id: int
    series_id: int
    episode_ids: Optional[List[int]]
    source_title: Optional[str]
    languages: Optional[List[Language]]
    quality: QualityModel
    custom_formats: Optional[List[CustomFormatResource]]
    date: str
    protocol: DownloadProtocol
    indexer: Optional[str]
    message: Optional[str]
    series: SeriesResource
