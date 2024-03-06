"""
Test sequence module
"""
import copy
import pytest
from pydantic import ValidationError
from replay_wizard.models import KeyboardAction, Sequence


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


def test_add_true_time(true_time_sequence, put_a_action):
    """
    Test add method
    """
    true_time_sequence.add(put_a_action)


def test_sequence_is_frozen(empty_sequence):
    """
    Test that sequence is frozen (immutable)
    """
    with pytest.raises(ValidationError):
        empty_sequence.true_time = True


def test_to_dict(empty_sequence, put_a_action, put_a_action_dict, mouse_action, mouse_action_dict):
    """
    Test sequence to dict
    """
    result = {
        'name': 'open youtube',
        'actions': [],
        # 'true_time': False,
    }
    assert result == empty_sequence.model_dump()
    empty_sequence.add(put_a_action)
    empty_sequence.add(mouse_action)

    result['actions'] = [
        put_a_action_dict,
        mouse_action_dict,
    ]

    assert result == empty_sequence.model_dump()


def test_in(empty_sequence, put_a_action):
    """
    Test in method
    """
    assert (put_a_action in empty_sequence) is False
    empty_sequence.add(put_a_action)
    assert put_a_action in empty_sequence


def test_for(one_action_sequence, put_a_action):
    """
    Test for method
    """
    one_action_sequence.add(put_a_action)
    one_action_sequence.add(put_a_action)
    count = 0
    for action in one_action_sequence:
        count += 1
        assert isinstance(action, KeyboardAction)
    assert count == len(one_action_sequence)


def test_getitem(one_action_sequence, put_a_action):
    """
    Test for []
    """
    sequence_put_a_action = one_action_sequence[0]
    assert sequence_put_a_action == put_a_action


def test_update(one_action_sequence):
    """
    test update method
    """
    other_sequence = copy.deepcopy(one_action_sequence)
    one_action_sequence.update(other_sequence)
    assert len(one_action_sequence) == 2


def test_combine(one_action_sequence):
    """
    Test combine many sequences
    """
    other_sequence = copy.deepcopy(one_action_sequence)
    new_sequence = Sequence.combine('combined',one_action_sequence, other_sequence)
    assert new_sequence.name == 'combined'
    assert len(new_sequence) == 2
