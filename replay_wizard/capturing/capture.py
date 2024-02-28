"""
Capture process module
"""
import json
import pynput
from replay_wizard.models import Sequence
from .keyboard import on_press, on_release


def capture(name):
    """
    capture user actions

    :param name: sequence name
    """
    sequence = Sequence(
        name=name
    )

    def on_press_handler(key):
        return on_press(sequence, key)

    def on_release_handler(key):
        return on_release(sequence, key)

    with pynput.keyboard.Listener(
            on_press=on_press_handler,
            on_release=on_release_handler) as listener:
        listener.join()

    # save result
    result_dict = sequence.model_dump()
    file_name = f'{name}.sequence'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f)
