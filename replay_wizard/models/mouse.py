"""
Mouse actions
"""
from enum import Enum
from pydantic import BaseModel, ConfigDict


class Button(str, Enum):
    """
    Mouse button
    """
    LEFT = 'left'
    RIGHT = 'right'


class MouseAction(BaseModel):
    """
    Mouse Action
    """
    model_config = ConfigDict(frozen=True)

    x: int
    y: int


class ScrollAction(MouseAction):
    """
    Scroll mouse action
    """
    dx: int
    dy: int


class ClickAction(MouseAction):
    """
    Click mouse action
    """
    button: Button
    pressed: bool
