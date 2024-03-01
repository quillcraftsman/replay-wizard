"""
Pytest fixtures
"""
from pytest import fixture
from replay_wizard.models import Action, Subtypes, Sequence, ActionEnum


@fixture
def put_a_action():
    """
    Simple action fixture
    """
    return Action(
        subtype=Subtypes.KEYBOARD,
        value='a',
        timedelta=0.1,
    )


@fixture
def put_enter_action():
    """
    Simple action fixture
    """
    action = Action(
        subtype=Subtypes.KEYBOARD,
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
    return Sequence(
        name='open youtube',
        actions=[]
    )


@fixture
def one_action_sequence(empty_sequence, put_a_action):
    """
    sequence with one action
    """

    empty_sequence.add(put_a_action)
    return empty_sequence
