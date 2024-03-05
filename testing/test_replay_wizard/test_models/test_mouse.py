"""
Test mouse models
"""
import pytest
from pydantic import ValidationError

from replay_wizard.models.mouse import (
    MouseAction,
    ScrollAction,
    ClickAction,
    Button,
)


def test_frozen():
    """
    Test MouseAction is frozen
    """
    actions = [
        MouseAction(x=0, y=0),
        ScrollAction(x=0, y=0, dx=0, dy=0),
        ClickAction(x=0, y=0, button=Button.LEFT, pressed=True)
    ]
    for action in actions:
        with pytest.raises(ValidationError):
            action.x = 5


def test_to_dict(mouse_action_dict, mouse_action):
    """
    Test mouse action to dict
    """
    assert mouse_action_dict == mouse_action.model_dump()
