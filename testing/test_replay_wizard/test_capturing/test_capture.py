"""
Test capture module
"""
from unittest import mock

import pynput.mouse
from pynput.keyboard import Key
from replay_wizard.capturing import capture


class MockListener:
    """
    Mock object for pynput Listener
    """

    def __init__(self, on_press, on_release):
        """
        Mock listener init mock
        """
        self.on_press = on_press
        self.on_release = on_release

    def join(self):
        """
        Thread join mock
        """
        self.on_press(Key.esc)
        self.on_release(Key.esc)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def start(self):
        """
        Mock start method
        """


class MouseMockListener:
    """
    Mouse Listener Mock
    """

    def __init__(self, on_move, on_scroll, on_click):
        """
        Mock listener init mock
        """
        self.on_move = on_move
        self.on_scroll = on_scroll
        self.on_click = on_click

    def join(self):
        """
        Thread join mock
        """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def start(self):
        """
        Mock start method
        """
        self.on_move(1, 1)
        self.on_scroll(1, 1, 1, 1)
        self.on_click(1, 1, pynput.mouse.Button.left, True)


def test_capture():
    """
    Test capture functions with mock
    """
    with mock.patch('pynput.keyboard.Listener', MockListener):
        sequence = capture('for_test')
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', MockListener):
        sequence = capture('for_test', non_blocking_mode=True)
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', MockListener):
        sequence = capture('for_test', keyboard=False)
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', MockListener):
        with mock.patch('pynput.mouse.Listener', MouseMockListener):
            sequence = capture('for_test', mouse=True)
            assert sequence.name == 'for_test'
        with mock.patch('pynput.mouse.Listener', MouseMockListener):
            sequence = capture('for_test', mouse=True)
            assert sequence.name == 'for_test'
