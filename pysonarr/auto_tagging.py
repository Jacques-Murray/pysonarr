"""
This module is used to automatically tag files in Sonarr.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from pysonarr.client import SonarrClient


@dataclass
class SelectOption:
    """
    Select option
    """

    value: int
    name: Optional[str]
    order: int
    hint: Optional[str]


class PrivacyLevel(Enum):
    """
    Privacy level
    """

    NORMAL = "normal"
    PASSWORD = "password"
    API_KEY = "apiKey"
    USER_NAME = "userName"


@dataclass
class Field:
    """
    Field
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
    place_holder: Optional[str]
    is_float: bool


@dataclass
class AutoTaggingSpecificationSchema:
    """
    Auto tagging specification schema
    """

    id: int
    name: Optional[str]
    implementation: Optional[str]
    implementation_name: Optional[str]
    negate: bool
    required: bool
    fields: Optional[List[Field]]


@dataclass
class AutoTaggingResource:
    """
    Auto tagging resource
    """

    id: int
    name: Optional[str]
    remove_tags_automatically: bool
    tags: Optional[List[int]]
    specifications: Optional[List[AutoTaggingSpecificationSchema]]


class AutoTagging:
    """
    Automatically tag files in Sonarr
    """

    def __init__(self, sonarr_client: SonarrClient):
        """
        Initialize the auto tagging module
        """
        self.sonarr_client = sonarr_client

    def post_auto_tagging(
        self, auto_tagging_resource: AutoTaggingResource = None
    ) -> AutoTaggingResource:
        """
        Post an auto tagging request to Sonarr
        """
        return self.sonarr_client.post(
            "/api/v3/autoTagging", json=auto_tagging_resource.to_dict()
        )

    def get_auto_tagging(self) -> List[AutoTaggingResource]:
        """
        Get auto tagging resources from Sonarr
        """

        return self.sonarr_client.get("/api/v3/autotagging")

    def put_auto_tagging(
        self,
        auto_tagging_id: int = 0,
        auto_tagging_resource: AutoTaggingResource = None,
    ) -> AutoTaggingResource:
        """
        Put an auto tagging request to Sonarr
        """

        return self.sonarr_client.put(
            f"/api/v3/autotagging/{auto_tagging_id}",
            json=auto_tagging_resource.to_dict(),
        )

    def delete_auto_tagging(self, auto_tagging_id: int = 0) -> int:
        """
        Delete an auto tagging request from Sonarr
        """

        return self.sonarr_client.delete(
            f"/api/v3/autotagging/{auto_tagging_id}"
        ).status_code

    def get_auto_tagging_by_id(self, auto_tagging_id: int = 0) -> AutoTaggingResource:
        """
        Get an auto tagging resource by ID from Sonarr
        """

        return self.sonarr_client.get(f"/api/v3/autotagging/{auto_tagging_id}")

    def get_auto_tagging_schema(self) -> int:
        """
        Get the auto tagging schema from Sonarr
        """

        return self.sonarr_client.get("/api/v3/autotagging/schema")
