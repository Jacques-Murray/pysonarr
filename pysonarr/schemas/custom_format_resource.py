"""
Sonarr Custom Format Resource Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.schemas.custom_format_specification_schema import (
    CustomFormatSpecificationSchema,
)


@dataclass
class CustomFormatResource:
    """
    Sonarr Custom Format Resource Schema
    """

    id: int
    name: Optional[str]
    include_custom_format_when_renaming: Optional[bool]
    specifications: Optional[List[CustomFormatSpecificationSchema]]
