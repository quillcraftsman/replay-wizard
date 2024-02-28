"""
Test keyboard module
"""
import pytest
from pynput.keyboard import Key, KeyCode

from replay_wizard.capturing.errors import UnknownKeyError
from replay_wizard.capturing.keyboard import on_press, key_to_value
from replay_wizard.models import Action, Sequence, Subtypes, ActionEnum


def test_on_press():
    """
    Test press function
    """
    sequence = Sequence(name='test on press')
    assert len(sequence) == 0
    on_press(sequence, Key.enter)
    assert len(sequence) == 1
    result_action = Action(
        subtype=Subtypes.KEYBOARD,
        value='enter',
        timedelta=0,
        action=ActionEnum.PRESS
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
