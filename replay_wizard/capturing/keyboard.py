"""
Capturing keyboard events
"""
import pynput
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.models import ActionEnum, KeyboardAction


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


def on_key_input(sequence, key, action_type: ActionEnum, exit_only=False):
    """
    Key input

    :param sequence: current sequence
    :param key: pressed key
    :param action: action type
    """

    value = key_to_value(key)
    if value is None:
        # Some keys haven't got char (shift for example)
        # We just skip this event now
        return True

    if value == 'esc':
        return False

    if not exit_only:
        action = KeyboardAction(
            value=key_to_value(key),
            action=action_type,
            timedelta=0,
        )
        sequence.add(action)
    return True


def on_press(sequence, key, exit_only=False):
    """
    Key was pressed

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.PRESS, exit_only=exit_only)


def on_release(sequence, key, exit_only=False):
    """
    Key was release

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.RELEASE, exit_only=exit_only)


def capture(sequence, non_blocking_mode=False, exit_only=False):
    """
    capture user keyboard actions

    :param sequence: current sequence
    :param non_blocking_mode: use non-blocking threading mode. Default = false
    """

    def on_press_handler(key):
        return on_press(sequence, key, exit_only=exit_only)

    def on_release_handler(key):
        return on_release(sequence, key, exit_only=exit_only)

    if non_blocking_mode:
        listener = pynput.keyboard.Listener(
            on_press=on_press_handler,
            on_release=on_release_handler)
        listener.start()
    else:
        with pynput.keyboard.Listener(
                on_press=on_press_handler,
                on_release=on_release_handler) as listener:
            listener.join()
