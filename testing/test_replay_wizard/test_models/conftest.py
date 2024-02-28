"""
Pytest fixtures
"""
from pytest import fixture
from replay_wizard.models import Action, Subtypes


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
def put_a_action_dict():
    """
    Action as dict fixture
    """
    return {
        'value': 'a',
        'subtype': 'keyboard',
        'timedelta': 0.1,
    }
