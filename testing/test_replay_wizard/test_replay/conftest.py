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


class MockMouseController:
    """
    Mock class for pynput mouse Controller
    """

    action_list = []

    def __init__(self):
        self.position = None

    def __setattr__(self, key, value):
        if key == 'position' and value is not None:
            self.action_list.append('MouseMove')

    def press(self, button):
        """
        Mock press method
        """
        self.action_list.append(f'ClickAction ({button})')

    def release(self, button):
        """
        Mock release method
        """
        self.action_list.append(f'ClickAction ({button})')

    def scroll(self, dx, dy):
        """
        Mock scroll method
        """
        self.action_list.append(f'ScrollAction({dx},{dy})')

    @classmethod
    def clear(cls):
        """
        Clear action lint after testing
        Because it's class property
        """
        cls.action_list.clear()


@fixture
def mocked_mouse_controller():
    """
    Mock keyboard kontroller from pynput
    """
    return MockMouseController
