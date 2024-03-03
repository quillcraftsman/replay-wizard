"""
Capture process module
"""
import pynput
from replay_wizard.capturing.keyboard import on_press, on_release
from replay_wizard.models import get_sequence


def capture(name, true_time=False, non_blocking_mode=False):
    """
    capture user actions

    :param name: sequence name
    :param true_time: save or not sequence with true time. default = False
    :param non_blocking_mode: use non-blocking threading mode. Default = false
    """
    Sequence = get_sequence(true_time=true_time)
    sequence = Sequence(
        name=name,
    )

    def on_press_handler(key):
        return on_press(sequence, key)

    def on_release_handler(key):
        return on_release(sequence, key)

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

    return sequence
