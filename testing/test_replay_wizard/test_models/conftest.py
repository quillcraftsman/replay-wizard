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
        'subtype': 'KeyboardAction',
        'action': 'press'
    }

@fixture
def mouse_action_dict():
    """
    Mouse action as dict fixture
    """
    return {
        'x': 0,
        'y': 0,
        'subtype': 'MouseAction',
    }


@fixture
def sequence_dict():
    """
    Sequence dict fixture
    """
    result = {
        'name': 'open youtube',
        'actions': [],
        'timestamp_list': [],
        'subtype': 'TimeSequence',
    }
    return result
