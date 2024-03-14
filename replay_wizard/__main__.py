"""
Package console entrypoint
"""
from replay_wizard.cli import capture_cli, replay_cli, combine_cli, sequence_list_cli


def capture():
    """
    capture CLI
    """
    capture_cli()


def replay():
    """
    replay CLI
    """
    replay_cli()


def combine():
    """
    combine CLI
    """
    combine_cli()


def sequence_list():
    """
    sequence list CLI
    """
    sequence_list_cli()
