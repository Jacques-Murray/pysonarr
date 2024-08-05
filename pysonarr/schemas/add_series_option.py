"""
Pysonarr Add Series Option Schema
"""

from dataclasses import dataclass

from pysonarr.enums.monitor_types import MonitorTypes


@dataclass
class AddSeriesOption:
    """
    Pysonarr Add Series Option Schema
    """

    ignore_episodes_with_files: bool
    ignore_episodes_without_files: bool
    monitor: MonitorTypes
    search_for_missing_episodes: bool
    search_for_cutoff_unmet_episodes: bool
