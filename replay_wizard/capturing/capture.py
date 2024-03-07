"""
Capture process module
"""
from replay_wizard.capturing.keyboard import capture as capture_keyboard
from replay_wizard.capturing.mouse import capture as capture_mouse
from replay_wizard.models import get_sequence


def capture(name, non_blocking_mode=False, keyboard=True, mouse=True):
    """
    capture user actions

    :param name: sequence name
    :param true_time: save or not sequence with true time. default = False
    :param non_blocking_mode: use non-blocking threading mode. Default = false
    :param keyboard: capture keyboard actions. default = True
    :param mouse: capture mouse actions. default = False
    """
    Sequence = get_sequence()
    sequence = Sequence(
        name=name,
    )

    if mouse:
        capture_mouse(sequence)

    if keyboard:
        capture_keyboard(sequence, non_blocking_mode)
    else:
        capture_keyboard(sequence, non_blocking_mode, exit_only=True)

    return sequence
