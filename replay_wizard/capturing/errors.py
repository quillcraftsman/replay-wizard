"""
Capturing Errors
"""


class UnknownKeyError(Exception):
    """
    Input key was unknown (pynput return None)
    """

    def __str__(self):
        """
        Exception to str
        """
        return 'Key was unknown (None value)'
