"""
Sonarr Backup Resource Schema
"""

from dataclasses import dataclass
from typing import Optional

from pysonarr.enums.backup_type import BackupType


@dataclass
class BackupResource:
    """
    Sonarr Backup Resource Schema
    """

    id: int
    name: Optional[str]
    path: Optional[str]
    backup_type: BackupType
    size: int
    time: str
