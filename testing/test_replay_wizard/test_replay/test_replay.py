"""
Test core module
"""
from unittest import mock
from replay_wizard.replay.replay import (
    replay,
    compare,
)


def test_replay_sequence(one_action_sequence, mocked_keyboard_controller):
    """
    Test replay function
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller) as mock_controller:
        replay(one_action_sequence)
        mock_controller.clear()


def test_replay_action(put_a_action, mocked_keyboard_controller):
    """
    Test replay one action
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller) as mock_controller:
        replay(put_a_action)
        mock_controller.clear()


MOCKED_TIME = 1709386168.5847345


def test_replay_schedule_strategy_empty(true_time_sequence, mocked_keyboard_controller):
    """
    Test replay with schedule strategy
    """
    with mock.patch('time.time') as mock_time:
        mock_time.return_value = MOCKED_TIME
        with mock.patch(
                'pynput.keyboard.Controller', mocked_keyboard_controller
        ) as mock_controller:
            replay(true_time_sequence, true_time=True)
            mock_controller.clear()


def test_replay_schedule_strategy(true_time_sequence, put_a_action, mocked_keyboard_controller):
    """
    Test replay with schedule strategy
    """
    true_time_sequence.add(put_a_action)
    with mock.patch(
            'pynput.keyboard.Controller', mocked_keyboard_controller
    ) as mock_controller:
        replay(true_time_sequence, true_time=True)
        mock_controller.clear()


def test_compare(true_time_sequence, put_a_action):
    """
    Test compare two sequences
    """
    true_time_sequence.add(put_a_action)
    true_time_sequence.add(put_a_action)
    assert compare(true_time_sequence, true_time_sequence) == 0
