"""
Test CLI parser
"""
import argparse

import pytest
from replay_wizard.cli.parser import str2bool


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, True),
        ('yes', True),
        ('true', True),
        ('t', True),
        ('y', True),
        ('1', True),
        (False, False),
        ('no', False),
        ('false', False),
        ('f', False),
        ('n', False),
        ('0', False),
    ]
)
def test_str2bool(value, expected):
    """
    test str2bool
    """
    assert str2bool(value) is expected


def test_str2bool_error():
    """
    Test str2bool
    """
    with pytest.raises(argparse.ArgumentTypeError):
        str2bool('not bool value')
