"""
Sonarr Custom Format Specification Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.schemas.field import Field


@dataclass
class CustomFormatSpecificationSchema:
    """
    Sonarr Custom Format Specification Schema
    """

    id: int
    name: Optional[str]
    implementation: Optional[str]
    implementation_name: Optional[str]
    info_link: Optional[str]
    negate: bool
    required: bool
    fields: Optional[List[Field]]
    presets: Optional[List[dict]]
