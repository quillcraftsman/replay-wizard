"""
Utils module (need refactoring)
"""
from .keyboard import KeyboardAction
from .mouse import (
    MouseAction,
    ScrollAction,
    ClickAction,
)


def get_action(subtype: str):
    """
    Get Action class by subtype (classname)
    """
    action_types = [
        KeyboardAction,
        MouseAction,
        ScrollAction,
        ClickAction,
    ]
    action_types_dict = {
        item.__name__: item
        for item in action_types
    }
    return action_types_dict[subtype]
