"""
Test mouse module
"""
from unittest import mock

from replay_wizard.replay.mouse import move_mouse, click_mouse, scroll_action
from replay_wizard.models.mouse import ClickAction, ScrollAction, Button


def test_move(mouse_action, mocked_mouse_controller):
    """
    Test push button function
    """
    with mock.patch('pynput.mouse.Controller', mocked_mouse_controller) as mock_controller:
        assert len(mock_controller.action_list) == 0
        move_mouse(mouse_action)
        assert len(mock_controller.action_list) == 1

        click = ClickAction(
            x=0,
            y=0,
            pressed=True,
            button=Button.LEFT,
        )

        click_mouse(click)
        # 3 because first controller move mouse
        assert len(mock_controller.action_list) == 3

        click = ClickAction(
            x=0,
            y=0,
            pressed=False,
            button=Button.LEFT,
        )

        click_mouse(click)
        # 3 because first controller move mouse
        assert len(mock_controller.action_list) == 5

        scroll = ScrollAction(
            x=0,
            y=0,
            dx=0,
            dy=0,
        )

        scroll_action(scroll)

        # 7 because move mouse first
        assert len(mock_controller.action_list) == 7

        mock_controller.clear()
