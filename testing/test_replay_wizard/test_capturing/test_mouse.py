"""
Test mouse function
"""
from replay_wizard.capturing.mouse import (
    on_move,
    on_scroll,
    on_click,
)


def test_on_move(empty_sequence):
    """
    Test on_move handler
    """
    on_move(empty_sequence, 1, 1)
    assert len(empty_sequence) == 1
    action = empty_sequence.actions[0]
    assert action.x == 1


def test_on_scroll(empty_sequence):
    """
    Test on scroll
    """
    on_scroll(empty_sequence, 1, 1, 1, 1)
    assert len(empty_sequence) == 1
    assert empty_sequence[0].dx == 1


def test_on_click(empty_sequence):
    """
    Test on mouse click
    """
    on_click(empty_sequence, 1, 1, 'left', True)
    assert len(empty_sequence) == 1
    assert empty_sequence[0].pressed
