"""
Tests for timesequence
"""
from unittest import mock

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


def test_to_dict(true_time_sequence, put_a_action, put_a_action_dict):
    """
    Test sequence to dict
    """
    result = {
        'name': 'open youtube',
        'actions': [],
        'timestamp_list': []
    }
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


# def test_is_valid_timestamps(true_time_sequence, put_a_action):
#     assert true_time_sequence.is_valid_timestamps()
#     true_time_sequence.add(put_a_action)
#     assert true_time_sequence.is_valid_timestamps()
#     true_time_sequence.timestamp_list.append(1)
#     assert true_time_sequence.is_valid_timestamps() is False
