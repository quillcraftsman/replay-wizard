"""
Action module
"""
from enum import Enum
from .action import Action


class ActionEnum(str, Enum):
    """
    press or release
    """
    PRESS = 'press'
    RELEASE = 'release'


class KeyboardAction(Action):
    """
    Action model
    """
    value: str
    action: ActionEnum = ActionEnum.PRESS
    subtype: str = 'KeyboardAction'
