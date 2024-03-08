"""
Pytest fixtures
"""
from pytest import fixture
import pynput
from pynput.keyboard import Key
from replay_wizard.models import KeyboardAction, ActionEnum, get_sequence, MouseAction


@fixture
def mouse_action():
    """
    Mouse action
    """
    return MouseAction(x=0, y=0)


@fixture
def put_a_action():
    """
    Simple action fixture
    """
    return KeyboardAction(
        value='a',
        timedelta=0.1,
    )


@fixture
def put_enter_action():
    """
    Simple action fixture
    """
    action = KeyboardAction(
        value='enter',
        timedelta=0.1,
        action=ActionEnum.RELEASE
    )
    return action


@fixture
def empty_sequence():
    """
    Empty sequence fixture
    """
    Sequence = get_sequence()
    return Sequence(
        name='open youtube',
        actions=[]
    )


@fixture
def true_time_sequence():
    """
    Empty sequence with true time fixture
    """
    TimeSequence = get_sequence()
    return TimeSequence(
        name='open youtube',
        actions=[],
        true_time=True,
        start_time=0,
    )


@fixture
def one_action_sequence(empty_sequence, put_a_action):
    """
    sequence with one action
    """

    empty_sequence.add(put_a_action)
    return empty_sequence



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


@fixture
def mock_listener():
    """
    Mock keyboard Listener
    """
    return MockListener


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


@fixture
def mouse_mock_listener():
    """
    Mouse mock listener fixture
    """
    return MouseMockListener


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
