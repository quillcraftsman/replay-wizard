"""
Test utils CLI module
"""
from unittest import mock
from replay_wizard.cli.utils import is_sequence_file, show_sequences, sequence_list_cli


def test_is_sequence_file():
    """
    Test is_sequence_file
    """
    assert is_sequence_file('one.txt', 'txt', lambda x: True)
    assert is_sequence_file('one.txt', 'txt', lambda x: False) is False
    assert is_sequence_file('one.other', 'txt', lambda x: True) is False


def test_show_sequences():
    """
    test show sequences
    """
    def show(name):
        show.count += 1
        show.files.append(name)

    show.count = 0
    show.files = []

    def is_file(name):
        return '.' in name

    all_files = ['one.s', 'two.s', 'dir', 'three.m']
    show_sequences(all_files, 's', is_file, show)
    assert show.count == 2
    assert show.files == ['one.s', 'two.s']


def test_sequence_list_cli(mock_list_argument_parser):
    """
    Test CLI
    """
    with mock.patch('argparse.ArgumentParser', mock_list_argument_parser):
        with mock.patch('os.listdir'):
            with mock.patch('os.path.isfile'):
                sequence_list_cli()
