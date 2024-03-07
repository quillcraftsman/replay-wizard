"""
Storage package
"""
import json
from replay_wizard.models import get_sequence

DEFAULT_EXTENSION = 'sequence'


def create_filename(sequence_name, extension=DEFAULT_EXTENSION):
    """
    Create filename

    :param sequence_name: current sequence name
    :param extension: file extension. default = sequence
    """
    return f'{sequence_name}.{extension}'


def save_to_file(sequence, extension=DEFAULT_EXTENSION):
    """
    Save sequence to file
    """
    result_dict = sequence.model_dump()
    file_name = create_filename(sequence.name, extension)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f)


def load_from_file(sequence_name, extension=DEFAULT_EXTENSION):
    """
    Load sequence from file
    """
    filename = create_filename(sequence_name, extension)
    with open(filename, 'r', encoding='utf-8') as f:
        sequence_dict = json.load(f)
        Sequence = get_sequence()
        sequence = Sequence.model_validate(sequence_dict)
        return sequence
