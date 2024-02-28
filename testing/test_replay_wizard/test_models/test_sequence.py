"""
Test sequence module
"""
import pytest
from replay_wizard.models import Action, Sequence, Subtypes


@pytest.fixture
def empty_sequence():
    """
    Empty sequence fixture
    """
    return Sequence(
        name='open youtube',
        actions=[]
    )


def test_full_sequence(put_a_action):
    """
    Test full sequence data
    """
    put_b = Action(
        subtype=Subtypes.KEYBOARD,
        value='b',
        timedelta=0.1,
    )
    Sequence(
        name='input a then b',
        actions=[put_a_action, put_b]
    )


def test_len(empty_sequence):
    """
    Test __len__ method
    """
    assert len(empty_sequence) == 0


def test_add(empty_sequence, put_a_action):
    """
    Test add method
    """
    assert len(empty_sequence) == 0
    empty_sequence.add(put_a_action)
    assert len(empty_sequence) == 1


def test_to_dict(empty_sequence, put_a_action, put_a_action_dict):
    """
    Test sequence to dict
    """
    result = {
        'name': 'open youtube',
        'actions': [],
    }
    assert result == empty_sequence.model_dump()
    empty_sequence.add(put_a_action)

    result['actions'] = [
        put_a_action_dict
    ]

    assert result == empty_sequence.model_dump()


def test_in(empty_sequence, put_a_action):
    """
    Test in method
    """
    assert (put_a_action in empty_sequence) is False
    empty_sequence.add(put_a_action)
    assert put_a_action in empty_sequence
