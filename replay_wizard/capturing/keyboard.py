"""
Capturing keyboard events
"""
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.models import Sequence, ActionEnum, Action, Subtypes


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


def on_key_input(sequence: Sequence, key, action_type: ActionEnum):
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


def on_press(sequence: Sequence, key):
    """
    Key was pressed

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.PRESS)


def on_release(sequence: Sequence, key):
    """
    Key was release

    :param sequence: current sequence
    :param key: pressed key
    """
    return on_key_input(sequence, key, ActionEnum.RELEASE)

#
#
# def on_release(key, f):
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#     print('{0} released'.format(
#         key))
#     f.write(f'{key.char} released\n')
#
#
# def capture(name):
#     file_name = f'{name}.sequence'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         on_press_handler = lambda key: on_press(key, f)
#         on_release_handler = lambda key: on_release(key, f)
#
#         with keyboard.Listener(
#                 on_press=on_press_handler,
#                 on_release=on_release_handler) as listener:
#             listener.join()
#
#     # ...or, in a non-blocking fashion:
#     # listener = keyboard.Listener(
#     #     on_press=on_press,
#     #     on_release=on_release)
#     # listener.start()
