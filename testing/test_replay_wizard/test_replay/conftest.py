"""
Pytest fixtures
"""
from pytest import fixture


class MockKeyboardController:
    """
    Mock class for pynput Controller
    """

    action_list = []

    def press(self, key):
        """
        Mocked press method
        """
        self.action_list.append(('PRESS', key))

    def release(self, key):
        """
        Mocked release method
        """
        self.action_list.append(('RELEASE', key))

    @classmethod
    def clear(cls):
        """
        Clear action lint after testing
        Because it's class property
        """
        cls.action_list.clear()


@fixture
def mocked_keyboard_controller():
    """
    Mock keyboard kontroller from pynput
    """
    return MockKeyboardController
