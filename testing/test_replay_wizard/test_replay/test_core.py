"""
Test core module
"""
from unittest import mock
from replay_wizard.replay.core import replay, replay_sequence, replay_action


def test_replay(mocked_keyboard_controller):
    """
    Test for replay function
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller):
        replay('sequence','testdata')


def test_replay_sequence(one_action_sequence, mocked_keyboard_controller):
    """
    Test replay function
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller) as mock_controller:
        replay_sequence(one_action_sequence)
        mock_controller.clear()


def test_replay_action(put_a_action, mocked_keyboard_controller):
    """
    Test replay one action
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller) as mock_controller:
        replay_action(put_a_action)
        mock_controller.clear()
