"""
pysonarr.enums
"""

from .apply_tags import ApplyTags
from .authentication_required_type import AuthenticationRequiredType
from .authentication_type import AuthenticationType
from .backup_type import BackupType
from .download_protocol import DownloadProtocol
from .media_cover_types import MediaCoverTypes
from .monitor_types import MonitorTypes
from .new_item_monitor_types import NewItemMonitorTypes
from .privacy_level import PrivacyLevel
from .quality_source import QualitySource
from .series_status_type import SeriesStatusType
from .series_types import SeriesTypes

__all__ = [
    "ApplyTags",
    "AuthenticationRequiredType",
    "AuthenticationType",
    "BackupType",
    "DownloadProtocol",
    "MediaCoverTypes",
    "MonitorTypes",
    "NewItemMonitorTypes",
    "PrivacyLevel",
    "QualitySource",
    "SeriesStatusType",
    "SeriesTypes",
]
