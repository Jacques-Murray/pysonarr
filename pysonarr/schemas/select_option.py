"""
Sonarr Select Option Schema
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SelectOption:
    """
    Sonarr Select Option Schema
    """

    value: int
    name: Optional[str]
    order: int
    hint: Optional[str]
