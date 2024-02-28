"""
Action module
"""
from enum import Enum
from pydantic import BaseModel, ConfigDict


class Subtypes(str, Enum):
    """
    Action subtype
    """
    KEYBOARD = 'keyboard'
    MOUSE = 'mouse'


class ActionEnum(str, Enum):
    """
    press or release
    """
    PRESS = 'press'
    RELEASE = 'release'


class Action(BaseModel):
    """
    Action model
    """
    model_config = ConfigDict(frozen=True)

    subtype: Subtypes
    value: str
    action: ActionEnum = ActionEnum.PRESS
