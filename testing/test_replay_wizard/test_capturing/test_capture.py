"""
Test capture module
"""
from unittest import mock
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


def test_capture():
    """
    Test capture functions with mock
    """
    with mock.patch('pynput.keyboard.Listener', MockListener):
        capture('for_test')
