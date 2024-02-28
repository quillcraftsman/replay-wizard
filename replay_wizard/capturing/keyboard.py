"""
Capturing keyboard events
"""
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.models import Sequence, ActionEnum, Action, Subtypes


# from pynput import keyboard
#
#
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


def on_press(sequence: Sequence, key):
    """
    Key was pressed

    :param key: pressed key
    """
    action = Action(
        subtype=Subtypes.KEYBOARD,
        value=key_to_value(key),
        action=ActionEnum.PRESS,
        timedelta=0,
    )
    sequence.add(action)
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
