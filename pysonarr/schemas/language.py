"""
Sonarr Language Schema
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Language:
    """
    Sonarr Language Schema
    """

    id: int
    name: Optional[str]
