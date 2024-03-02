"""
Pytest fixtures
"""
from pytest import fixture
from replay_wizard.models import Action, Subtypes, ActionEnum, get_sequence


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
    TimeSequence = get_sequence(true_time=True)
    return TimeSequence(
        name='open youtube',
        actions=[],
        true_time=True,
    )


@fixture
def one_action_sequence(empty_sequence, put_a_action):
    """
    sequence with one action
    """

    empty_sequence.add(put_a_action)
    return empty_sequence
