"""
Sonaar Series Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.enums.new_item_monitor_types import NewItemMonitorTypes
from pysonarr.enums.series_status_type import SeriesStatusType
from pysonarr.enums.series_types import SeriesTypes
from pysonarr.schemas.add_series_options import AddSeriesOptions
from pysonarr.schemas.alternate_title_resource import AlternateTitleResource
from pysonarr.schemas.language import Language
from pysonarr.schemas.media_cover import MediaCover
from pysonarr.schemas.ratings import Ratings
from pysonarr.schemas.season_resource import SeasonResource
from pysonarr.schemas.series_statistics_resource import SeriesStatisticsResource


@dataclass
class SeriesResource:
    """
    Sonarr Series Resource Schema
    """

    id: int
    title: Optional[str]
    alternate_titles: Optional[List[AlternateTitleResource]]
    sort_title: Optional[str]
    status: SeriesStatusType
    ended: bool
    profile_name: Optional[str]
    overview: Optional[str]
    next_airing: Optional[str]
    previous_airing: Optional[str]
    network: Optional[str]
    air_time: Optional[str]
    images: Optional[List[MediaCover]]
    original_language: Language
    remote_poster: Optional[str]
    seasons: Optional[List[SeasonResource]]
    year: int
    path: Optional[str]
    quality_profile_id: int
    season_folder: bool
    monitored: bool
    monitor_new_items: NewItemMonitorTypes
    use_scene_numbering: bool
    runtime: int
    tvdb_id: int
    tv_rage_id: int
    tv_maze_id: int
    tmdb_id: int
    first_aired: Optional[str]
    last_aired: Optional[str]
    series_type: SeriesTypes
    clean_title: Optional[str]
    imdb_id: Optional[str]
    title_slug: Optional[str]
    root_folder_path: Optional[str]
    folder: Optional[str]
    certification: Optional[str]
    genres: Optional[List[str]]
    tags: Optional[List[int]]
    added: str
    add_options: AddSeriesOptions
    ratings: Ratings
    statistics: SeriesStatisticsResource
    episodes_changed: Optional[bool]
