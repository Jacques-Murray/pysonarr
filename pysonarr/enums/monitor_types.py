"""
Sonarr Monitor Types
"""

from enum import Enum


class MonitorTypes(Enum):
    """
    Monitor Types
    """

    UNKNOWN = "unknown"
    ALL = "all"
    FUTURE = "future"
    MISSING = "missing"
    EXISTING = "existing"
    FIRST_SEASON = "firstSeason"
    LAST_SEASON = "lastSeason"
    LATEST_SEASON = "latestSeason"
    PILOT = "pilot"
    RECENT = "recent"
    MONITOR_SPECIALS = "monitorSpecials"
    UNMONITOR_SPECIALS = "unmonitorSpecials"
    NONE = "none"
    SKIP = "skip"
