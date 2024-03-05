"""
Mouse actions
"""
from enum import Enum
from .action import Action


class Button(str, Enum):
    """
    Mouse button
    """
    LEFT = 'left'
    RIGHT = 'right'


class MouseAction(Action):
    """
    Mouse Action
    """
    x: int
    y: int
    subtype: str = 'MouseAction'


class ScrollAction(MouseAction):
    """
    Scroll mouse action
    """
    dx: int
    dy: int
    subtype: str = 'ScrollAction'


class ClickAction(MouseAction):
    """
    Click mouse action
    """
    button: Button
    pressed: bool
    subtype: str = 'ClickAction'
