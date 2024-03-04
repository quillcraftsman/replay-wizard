"""
Mouse events capturing
"""
import pynput
from replay_wizard.models import (
    MouseAction,
    ScrollAction,
    ClickAction,
    Button,
)


def on_move(sequence, x, y):
    """
    On mouse move

    :param sequence: current sequence
    :param x: x mouse new position
    :param y: y mouse new position
    """
    action = MouseAction(x=x, y=y)
    sequence.add(action)


def on_scroll(sequence, x, y, dx, dy):
    """
    On scroll

    :param sequence: current sequence
    :param x: x mouse position
    :param y: y mouse position
    :param dx: delta x
    :param dy: delta y
    """
    action = ScrollAction(
        x=x,
        y=y,
        dx=dx,
        dy=dy,
    )
    sequence.add(action)


def on_click(sequence, x, y, button, pressed):
    """
    On scroll

    :param sequence: current sequence
    :param x: x mouse position
    :param y: y mouse position
    :param button: left/right
    :param pressed: True/False
    """
    action = ClickAction(
        x=x,
        y=y,
        button=button,
        pressed=pressed,
    )
    sequence.add(action)


def capture(sequence):
    """
    capture user keyboard actions

    :param sequence: current sequence
    :param non_blocking_mode: use non-blocking threading mode. Default = false
    """

    def on_move_handler(x, y):
        return on_move(sequence, x, y)

    def on_scroll_handler(x, y, dx, dy):
        return on_scroll(sequence, x, y, dx, dy)

    def on_click_handler(x, y, button, pressed):
        buttons = {
            pynput.mouse.Button.left: Button.LEFT,
            pynput.mouse.Button.right: Button.RIGHT,
        }

        button = buttons[button]
        return on_click(sequence, x, y, button, pressed)

    # if non_blocking_mode:
    listener = pynput.mouse.Listener(
        on_move=on_move_handler,
        on_scroll=on_scroll_handler,
        on_click=on_click_handler,
    )
    listener.start()
    # else:
    #     with pynput.keyboard.Listener(
    #             on_move=on_move_handler,
    #             on_scroll=on_scroll_handler,
    #             on_click=on_click_handler,
    #     ) as listener:
    #         listener.join()
