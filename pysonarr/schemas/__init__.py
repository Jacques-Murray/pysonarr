"""
pysonarr.schemas
"""

from .add_series_options import AddSeriesOptions
from .alternate_title_resource import AlternateTitleResource
from .auto_tagging_resource import AutoTaggingResource
from .auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from .backup_resource import BackupResource
from .blocklist_bulk_resource import BlocklistBulkResource
from .blocklist_resource import BlocklistResource
from .custom_format_resource import CustomFormatResource
from .custom_format_specification_schema import CustomFormatSpecificationSchema
from .field import Field
from .language import Language
from .media_cover import MediaCover
from .quality import Quality
from .quality_model import QualityModel
from .ratings import Ratings
from .revision import Revision
from .season_resource import SeasonResource
from .season_statistics_resource import SeasonStatisticsResource
from .select_option import SelectOption
from .series_resource import SeriesResource
from .series_statistics_resource import SeriesStatisticsResource

__all__ = [
    "AddSeriesOptions",
    "AlternateTitleResource",
    "AutoTaggingResource",
    "AutoTaggingSpecificationSchema",
    "BackupResource",
    "BlocklistBulkResource",
    "BlocklistResource",
    "CustomFormatResource",
    "CustomFormatSpecificationSchema",
    "Field",
    "Language",
    "MediaCover",
    "Quality",
    "QualityModel",
    "Ratings",
    "Revision",
    "SeasonResource",
    "SeasonStatisticsResource",
    "SelectOption",
    "SeriesResource",
    "SeriesStatisticsResource",
]
