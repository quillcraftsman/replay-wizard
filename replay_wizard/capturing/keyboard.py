"""
Capturing keyboard events
"""
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.models import ActionEnum, Action, Subtypes


def key_to_value(key):
    """
    Convert key different types to action value

    :param key: key to convert
    """
    if isinstance(key, Key):
        _, name = str(key).split('.')
        return name
    if isinstance(key, KeyCode):
        return key.char
    if key is None:
        raise UnknownKeyError
    raise ValueError(key)


def on_key_input(sequence, key, action_type: ActionEnum):
    """
    Key input

    :param sequence: current sequence
    :param key: pressed key
    :param action: action type
    """
    value = key_to_value(key)
    if value == 'esc':
        return False

    action = Action(
        subtype=Subtypes.KEYBOARD,
        value=key_to_value(key),
        action=action_type,
        timedelta=0,
    )
    sequence.add(action)
    return True


def on_press(sequence, key):
    """
    Key was pressed

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.PRESS)


def on_release(sequence, key):
    """
    Key was release

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.RELEASE)
