"""
Custom exceptions for pysonarr
"""


class SonarrError(Exception):
    """
    Base class for Sonarr errors
    """

    def __init__(self, message):
        self.message = message
        super().__init__(message)
