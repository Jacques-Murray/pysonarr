"""
Sonarr Field Schema
"""

from dataclasses import dataclass
from typing import List, Optional

from pysonarr.enums.privacy_level import PrivacyLevel
from pysonarr.schemas.select_option import SelectOption


@dataclass
class Field:
    """
    Sonarr Field Schema
    """

    order: int
    name: Optional[str]
    label: Optional[str]
    unit: Optional[str]
    help_text: Optional[str]
    help_text_warning: Optional[str]
    help_link: Optional[str]
    value: Optional[dict]
    field_type: Optional[str]
    advanced: bool
    select_options: Optional[List[SelectOption]]
    select_options_provider_action: Optional[str]
    section: Optional[str]
    hidden: Optional[str]
    privacy: PrivacyLevel
    placeholder: Optional[str]
    is_float: bool
