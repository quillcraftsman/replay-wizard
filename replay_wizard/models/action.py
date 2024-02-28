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


class Action(BaseModel):
    """
    Action model
    """
    model_config = ConfigDict(frozen=True)

    subtype: Subtypes
    value: str
    timedelta: float
