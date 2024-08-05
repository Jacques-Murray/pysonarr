"""
Sonarr Auto Tagging Specification Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.schemas.field import Field


@dataclass
class AutoTaggingSpecificationSchema:
    """
    Sonarr Auto Tagging Specification Schema
    """

    id: int
    name: Optional[str]
    implementation: Optional[str]
    implementation_name: Optional[str]
    negate: bool
    required: bool
    fields: Optional[List[Field]]
