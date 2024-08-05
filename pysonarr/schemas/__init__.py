"""
pysonarr.schemas
"""

from .add_series_option import AddSeriesOption
from .alternate_title_resource import AlternateTitleResource
from .auto_tagging_resource import AutoTaggingResource
from .auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from .backup_resource import BackupResource
from .blocklist_bulk_resource import BlocklistBulkResource
from .field import Field
from .select_option import SelectOption

__all__ = [
    "AddSeriesOption",
    "AlternateTitleResource",
    "AutoTaggingResource",
    "AutoTaggingSpecificationSchema",
    "BackupResource",
    "BlocklistBulkResource",
    "Field",
    "SelectOption",
]
