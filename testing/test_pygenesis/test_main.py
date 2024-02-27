"""
Test main
"""
from replay_wizard import info


def test_info():
    """
    Test info
    :return: None
    """
    info_expected_text = ('This is the mock of ReplayWizard package: '
                          'https://github.com/quillcraftsman/replay-wizard')
    assert info() == info_expected_text
