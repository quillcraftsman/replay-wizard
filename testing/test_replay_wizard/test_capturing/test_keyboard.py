"""
Test keyboard module
"""
import pytest
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.capturing.keyboard import on_press, key_to_value, on_release, on_key_input
from replay_wizard.models import KeyboardAction, ActionEnum


def test_on_key_input_exit(empty_sequence):
    """
    Test then exit key was inputted
    """
    result = on_key_input(empty_sequence, Key.esc, ActionEnum.PRESS)
    assert result is False


def test_on_key_input_non_key(empty_sequence):
    """
    Test key input then key.char = None
    """

    class NotCharKey(KeyCode):
        """
        Some char without char
        """
        def __init__(self):
            self.char = None

    result = on_key_input(empty_sequence, NotCharKey(), ActionEnum.PRESS)
    assert result is True


def test_on_press(empty_sequence):
    """
    Test press function
    """
    sequence = empty_sequence
    assert len(sequence) == 0
    on_press(sequence, Key.enter)
    assert len(sequence) == 1
    result_action = KeyboardAction(
        value='enter',
        timedelta=0,
        action=ActionEnum.PRESS
    )
    assert result_action in sequence


def test_on_release(empty_sequence):
    """
    Test release function
    """
    sequence = empty_sequence
    assert len(sequence) == 0
    on_release(sequence, Key.enter)
    assert len(sequence) == 1
    result_action = KeyboardAction(
        value='enter',
        timedelta=0,
        action=ActionEnum.RELEASE
    )
    assert result_action in sequence


def test_key_to_value_key():
    """
    Test send Key
    """
    assert 'enter' == key_to_value(Key.enter)


def test_key_to_value_keycode():
    """
    Test send KeyCode
    """
    assert 'a' == key_to_value(KeyCode(char='a'))


def test_key_to_value_none():
    """
    Test send None
    """
    with pytest.raises(UnknownKeyError):
        key_to_value(None)


def test_wrong_value():
    """
    Test send wrong value
    """
    with pytest.raises(ValueError):
        key_to_value('some strange value')
