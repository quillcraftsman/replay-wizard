"""
Test capture CLI module
"""
from unittest import mock
from replay_wizard.cli.capture import capture_cli


def test_capture_cli(mock_argument_parser, mock_listener, mouse_mock_listener):
    """
    Test capture CLI
    """
    with mock.patch('argparse.ArgumentParser', mock_argument_parser):
        with mock.patch('pynput.keyboard.Listener', mock_listener):
            with mock.patch('pynput.mouse.Listener', mouse_mock_listener):
                capture_cli()
