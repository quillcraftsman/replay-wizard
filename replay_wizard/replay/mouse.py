"""
Mouse replay functions
"""
import pynput
from replay_wizard.models import MouseAction, ClickAction, ScrollAction, Button


def move_mouse(action: MouseAction):
    """
    Move mouse
    """
    mouse = pynput.mouse.Controller()
    mouse.position = (action.x, action.y)


def click_mouse(action: ClickAction):
    """
    Mouse click
    """
    mouse = pynput.mouse.Controller()
    move_mouse(action)
    button = action.button
    button = pynput.mouse.Button.left if button == Button.LEFT else pynput.mouse.Button.right
    if action.pressed:
        mouse.press(button)
    else:
        mouse.release(button)


def scroll_action(action: ScrollAction):
    """
    Scroll action
    """
    mouse = pynput.mouse.Controller()
    move_mouse(action)
    mouse.scroll(action.dx, action.dy)
