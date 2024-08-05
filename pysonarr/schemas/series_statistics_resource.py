"""
Sonarr Series Statistics Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SeriesStatisticsResource:
    """
    Sonarr Series Statistics Resource Schema
    """

    season_count: int
    episode_file_count: int
    episode_count: int
    total_episode_count: int
    size_on_disk: int
    release_groups: Optional[List[str]]
    percent_of_episodes: float
