"""
Sonarr Blocklist Bulk Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BlocklistBulkResource:
    """
    Sonarr Blocklist Bulk Resource Schema
    """

    ids: Optional[List[int]]
