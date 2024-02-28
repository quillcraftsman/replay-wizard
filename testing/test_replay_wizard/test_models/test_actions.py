"""
Test Action model module
"""
import pytest
from pydantic import ValidationError
from replay_wizard.models import Subtypes, ActionEnum, Action


def test_action(put_a_action):
    """
    Test simple action
    """
    assert put_a_action.value == 'a'
    assert put_a_action.subtype == Subtypes.KEYBOARD
    assert put_a_action.timedelta == 0.1
    assert put_a_action.action == ActionEnum.PRESS


def test_action_is_frozen(put_a_action):
    """
    Test that action is frozen (immutable)
    """
    with pytest.raises(ValidationError):
        put_a_action.value = 'b'


def test_to_dict(put_a_action, put_a_action_dict):
    """
    Test action to dict
    """
    assert put_a_action_dict == put_a_action.model_dump()


def test_eq(put_a_action):
    """
    Test compare two actions
    """
    same_action = Action(
        subtype=put_a_action.subtype,
        value=put_a_action.value,
        timedelta=put_a_action.timedelta,
        action=put_a_action.action,
    )
    assert put_a_action == same_action
    other_action = Action(
        subtype=put_a_action.subtype,
        value=put_a_action.value,
        timedelta=put_a_action.timedelta,
        action=ActionEnum.RELEASE,
    )
    assert put_a_action != other_action
