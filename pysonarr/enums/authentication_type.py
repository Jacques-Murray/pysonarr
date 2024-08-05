"""
Sonarr Authentication Type Enum
"""

from enum import Enum


class AuthenticationType(Enum):
    """
    Sonarr Authentication Type Enum
    """

    NONE = "none"
    BASIC = "basic"
    FORMS = "forms"
    EXTERNAL = "external"
