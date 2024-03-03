"""
Capture process module
"""
import pynput
from replay_wizard.capturing.keyboard import on_press, on_release
from replay_wizard.models import get_sequence
from replay_wizard.storage import save_to_file, DEFAULT_EXTENSION


def capture(name, extension=DEFAULT_EXTENSION, true_time=False):
    """
    capture user actions

    :param name: sequence name
    :param true_time: save or not sequence with true time. default = False
    """
    Sequence = get_sequence(true_time=true_time)
    sequence = Sequence(
        name=name,
        true_time=true_time,
    )

    def on_press_handler(key):
        return on_press(sequence, key)

    def on_release_handler(key):
        return on_release(sequence, key)

    with pynput.keyboard.Listener(
            on_press=on_press_handler,
            on_release=on_release_handler) as listener:
        listener.join()

    # listener = pynput.keyboard.Listener(
    #     on_press=on_press_handler,
    #     on_release=on_release_handler)
    # listener.start()

    # save result
    # result_dict = sequence.model_dump()
    # file_name = f'{name}.sequence'
    # with open(file_name, 'w', encoding='utf-8') as f:
    #     json.dump(result_dict, f)
    save_to_file(sequence, extension)
