"""
Tests for timesequence
"""
import copy
from unittest import mock

from replay_wizard.models import get_sequence

MOCKED_TIME = 1709386168.5847783


def test_get_current_timestamp(true_time_sequence):
    """
    Test get current timestamp method
    """
    with mock.patch('time.time') as mock_time:
        mock_time.return_value = MOCKED_TIME
        timestamp = true_time_sequence.get_current_timestamp()
        assert timestamp == MOCKED_TIME


def test_add(true_time_sequence, put_a_action):
    """
    Test add method
    """
    # TimeSequence = get_sequence(true_time=True)
    assert len(true_time_sequence.timestamp_list) == 0
    with mock.patch('time.time') as mock_time:
        mock_time.return_value = MOCKED_TIME
        true_time_sequence.add(put_a_action)
        assert len(true_time_sequence.timestamp_list) == 1
        timestamp = true_time_sequence.timestamp_list[0]
        assert timestamp == MOCKED_TIME


def test_to_dict(true_time_sequence, put_a_action, put_a_action_dict, sequence_dict):
    """
    Test sequence to dict
    """
    result = sequence_dict
    assert result == true_time_sequence.model_dump()

    with mock.patch('time.time') as mock_time:
        mock_time.return_value = MOCKED_TIME
        true_time_sequence.add(put_a_action)

        result['actions'] = [
            put_a_action_dict
        ]

        result['timestamp_list'] = [
            MOCKED_TIME
        ]

        assert result == true_time_sequence.model_dump()


def test_update(true_time_sequence, put_a_action):
    """
    Test update method
    """
    true_time_sequence.add(put_a_action)
    other = copy.deepcopy(true_time_sequence)
    true_time_sequence.update(other)
    assert len(true_time_sequence) == 2
    assert len(true_time_sequence.timestamp_list) == 2


def test_model_validate(true_time_sequence, put_a_action):
    """
    Test model validate method
    """
    true_time_sequence.add(put_a_action)
    sequence_dict = true_time_sequence.model_dump()
    Sequence = get_sequence()
    sequence = Sequence.model_validate(sequence_dict)
    assert sequence == true_time_sequence


def test_model_validate_sequences(one_action_sequence, true_time_sequence):
    """
    Then sequences it's actions
    """
    Sequence = get_sequence()
    sequence = Sequence(name='combine')
    sequence.add(one_action_sequence)
    sequence.add(true_time_sequence)
    assert len(sequence) == 2
    sequence_dict = sequence.model_dump()
    assert isinstance(sequence_dict, dict)

    new_sequence = Sequence.model_validate(sequence_dict)
    assert isinstance(new_sequence, Sequence)
    assert len(new_sequence) == 2
    one, _ = new_sequence.actions
    assert isinstance(one, Sequence)
    assert one.name == one_action_sequence.name
    assert one.timestamp_list == one_action_sequence.timestamp_list
    assert one.actions == one_action_sequence.actions
