"""
Pytest fixtures
"""
import pytest
from replay_wizard.models import Sequence

@pytest.fixture
def empty_sequence():
    """
    Empty sequence fixture
    """
    return Sequence(
        name='open youtube',
        actions=[]
    )
