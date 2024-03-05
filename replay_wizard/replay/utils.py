"""
Replay utils (need refactoring)
"""
from .keyboard import push_button
from .mouse import move_mouse, click_mouse, scroll_action


def get_replayer(subtype: str):
    """
    Get replayer for action subtype
    """
    replayers = {
        'KeyboardAction': push_button,
        'MouseAction': move_mouse,
        'ClickAction': click_mouse,
        'ScrollAction': scroll_action,
    }
    return replayers[subtype]
