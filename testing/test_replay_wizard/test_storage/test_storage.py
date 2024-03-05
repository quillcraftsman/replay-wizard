"""
Test storage functions
"""
from pytest import fixture
from replay_wizard.storage import save_to_file, create_filename, DEFAULT_EXTENSION, load_from_file
from replay_wizard.models import get_sequence

SEQUENCE_NAME = 'test'

@fixture
def file_sequence(put_a_action, mouse_action):
    """
    Sequence to test saving
    """
    Sequence = get_sequence()
    sequence = Sequence(
        name=SEQUENCE_NAME,
        actions=[]
    )
    sequence.add(put_a_action)
    sequence.add(mouse_action)
    return sequence


def test_save_to_file(file_sequence):
    """
    Test save to file
    """
    save_to_file(file_sequence)
    with open(create_filename(file_sequence.name), 'r', encoding='utf-8') as f:
        assert file_sequence.name in f.read()


def test_create_filename():
    """
    Test create filename
    """
    assert create_filename(SEQUENCE_NAME) == f'{SEQUENCE_NAME}.{DEFAULT_EXTENSION}'
    assert create_filename(SEQUENCE_NAME, 'other') == f'{SEQUENCE_NAME}.other'


def test_load_from_file(put_a_action, mouse_action):
    """
    Test load from file
    """
    sequence = load_from_file(SEQUENCE_NAME)
    assert sequence.name == SEQUENCE_NAME
    assert len(sequence) == 2
    action = sequence[0]
    assert action == put_a_action
    action = sequence[1]
    assert action == mouse_action
