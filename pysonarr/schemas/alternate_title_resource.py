"""
Alternate Title Resource Schema
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AlternateTitleResource:
    """
    Alternate Title Resource Schema
    """

    title: Optional[str]
    season_number: Optional[int]
    scene_season_number: Optional[int]
    scene_origin: Optional[str]
    comment: Optional[str]
