"""
Sonarr Authentication Required Type Enum
"""

from enum import Enum


class AuthenticationRequiredType(Enum):
    """
    Authentication Required Type
    """

    ENABLED = "enabled"
    DISABLED_FOR_LOCAL_ADDRESSES = "disabledForLocalAddresses"
