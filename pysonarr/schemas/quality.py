"""
Sonarr Quality Schema
"""

from dataclasses import dataclass
from typing import Optional

from pysonarr.enums.quality_source import QualitySource


@dataclass
class Quality:
    """
    Sonarr Quality Schema
    """

    id: int
    name: Optional[str]
    source: QualitySource
    resolution: int
