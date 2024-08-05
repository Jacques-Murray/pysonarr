"""
Sonarr Ratings Schema
"""

from dataclasses import dataclass


@dataclass
class Ratings:
    """
    Sonarr Ratings Schema
    """

    votes: int
    value: float
