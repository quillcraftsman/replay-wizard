"""
Test keyboard module
"""
from unittest import mock
from pynput.keyboard import Key

from replay_wizard.replay.keyboard import push_button


def test_push_button(put_a_action, put_enter_action, mocked_keyboard_controller):
    """
    Test push button function
    """
    with mock.patch('pynput.keyboard.Controller', mocked_keyboard_controller) as mock_controller:
        assert len(mock_controller.action_list) == 0
        push_button(put_a_action)
        assert len(mock_controller.action_list) == 1
        action_type, key = mock_controller.action_list[0]
        assert action_type == 'PRESS'
        assert key == 'a'
        push_button(put_enter_action)
        assert len(mock_controller.action_list) == 2
        action_type, key = mock_controller.action_list[1]
        assert action_type == 'RELEASE'
        assert key == Key.enter
        mock_controller.clear()
