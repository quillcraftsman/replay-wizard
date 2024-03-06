"""
Test combine CLI module
"""
from unittest import mock
from replay_wizard.cli.combine import combine_cli


def test_combine_cli(mock_combine_argument_parser):
    """
    Test combine CLI
    """
    with mock.patch('argparse.ArgumentParser', mock_combine_argument_parser):
        combine_cli()
