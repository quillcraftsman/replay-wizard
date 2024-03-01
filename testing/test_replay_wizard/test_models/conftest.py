"""
Pytest fixtures
"""
from pytest import fixture


@fixture
def put_a_action_dict():
    """
    Action as dict fixture
    """
    return {
        'value': 'a',
        'subtype': 'keyboard',
        'action': 'press'
    }
