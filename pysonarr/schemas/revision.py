"""
Sonarr Revision Schema
"""

from dataclasses import dataclass


@dataclass
class Revision:
    """
    Sonarr Revision Schema
    """

    version: int
    real: int
    is_repack: bool
