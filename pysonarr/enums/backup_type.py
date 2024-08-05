"""
Sonarr Backup Type Enum
"""

from enum import Enum


class BackupType(Enum):
    """
    Sonarr Backup Type Enum
    """

    SCHEDULED = "scheduled"
    MANUAL = "manual"
    UPDATE = "update"
