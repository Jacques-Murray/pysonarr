"""
Sonarr Quality Model Schema
"""

from dataclasses import dataclass

from pysonarr.schemas.quality import Quality
from pysonarr.schemas.revision import Revision


@dataclass
class QualityModel:
    """
    Sonarr Quality Model Schema
    """

    quality: Quality
    revision: Revision
