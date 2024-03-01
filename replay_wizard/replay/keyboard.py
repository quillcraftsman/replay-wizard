"""
Keyboard replay functions
"""
import pynput
from pynput.keyboard import Key
from replay_wizard.models import Action


def push_button(action: Action):
    """
    Push keyboard button
    """
    value = action.value
    action_type = action.action
    try:
        value = Key[value]
    except KeyError:
        pass
    keyboard = pynput.keyboard.Controller()
    push_function = getattr(keyboard, action_type)
    push_function(value)
