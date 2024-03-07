"""
Models package
"""
from .keyboard import KeyboardAction, ActionEnum
# from .sequence import Sequence
from .time_sequence import TimeSequence
from .mouse import (
    MouseAction,
    ScrollAction,
    ClickAction,
    Button,
)


def get_sequence() -> TimeSequence:
    """
    Fabric method to get sequence object

    :param true_time: use true time
    """
    # return TimeSequence if true_time else Sequence
    return TimeSequence
