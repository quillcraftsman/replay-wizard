"""
Test capture module
"""
from unittest import mock
from replay_wizard.capturing import capture



def test_capture(mock_listener, mouse_mock_listener):
    """
    Test capture functions with mock
    """
    with mock.patch('pynput.keyboard.Listener', mock_listener):
        sequence = capture('for_test')
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', mock_listener):
        sequence = capture('for_test', non_blocking_mode=True)
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', mock_listener):
        sequence = capture('for_test', keyboard=False)
        assert sequence.name == 'for_test'

    with mock.patch('pynput.keyboard.Listener', mock_listener):
        with mock.patch('pynput.mouse.Listener', mouse_mock_listener):
            sequence = capture('for_test', mouse=True)
            assert sequence.name == 'for_test'
        with mock.patch('pynput.mouse.Listener', mouse_mock_listener):
            sequence = capture('for_test', mouse=True)
            assert sequence.name == 'for_test'
