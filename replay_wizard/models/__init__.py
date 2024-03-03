"""
Models package
"""
from .action import Action, Subtypes, ActionEnum
from .sequence import Sequence
from .time_sequence import TimeSequence


def get_sequence(true_time=False) -> Sequence:
    """
    Fabric method to get sequence object

    :param true_time: use true time
    """
    return TimeSequence if true_time else Sequence
