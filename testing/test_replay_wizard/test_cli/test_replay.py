"""
Test CLI replay module
"""
from unittest import mock
from replay_wizard.cli.replay import replay_cli


def test_replay_cli(
        mock_argument_parser,
        mock_listener,
        mouse_mock_listener,
        mocked_mouse_controller,
        mocked_keyboard_controller
):
    """
    Test CLI replay
    """
    with mock.patch('argparse.ArgumentParser', mock_argument_parser):
        with mock.patch('pynput.keyboard.Listener', mock_listener):
            with mock.patch('pynput.mouse.Listener', mouse_mock_listener):
                with mock.patch(
                        'pynput.keyboard.Controller', mocked_keyboard_controller) as keyboard_mock:
                    with mock.patch(
                            'pynput.mouse.Controller', mocked_mouse_controller) as mouse_mock:
                        replay_cli()
                        keyboard_mock.clear()
                        mouse_mock.clear()
