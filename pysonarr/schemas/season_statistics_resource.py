"""
Sonarr Season Statistics Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SeasonStatisticsResource:
    """
    Sonarr Season Statistics Resource Schema
    """

    next_airing: Optional[str]
    previous_airing: Optional[str]
    episode_file_count: int
    episode_count: int
    total_episode_count: int
    size_on_disk: int
    release_groups: Optional[List[str]]
    percent_of_episodes: float
