"""
Sonarr AutoTaggingResource Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.schemas.auto_tagging_specification_schema import (
    AutoTaggingSpecificationSchema,
)


@dataclass
class AutoTaggingResource:
    """
    Sonarr AutoTaggingResource Schema
    """

    id: int
    name: Optional[str]
    remove_tags_automatically: bool
    tags: Optional[List[int]]
    specifications: Optional[List[AutoTaggingSpecificationSchema]]
