"""
Replay core module
"""
import json
from replay_wizard.models import Sequence, Action
from .keyboard import push_button


def replay(name, extension='sequence'):
    """
    Replay sequence from file

    :param name: sequence name, without extension
    :param extension: sequence file extension
    """
    filename = f'{name}.{extension}'
    with open(filename, 'r', encoding='utf-8') as f:
        sequence_dict = json.load(f)
        sequence = Sequence.model_validate(sequence_dict)
        replay_sequence(sequence)


def replay_action(action: Action):
    """
    Replay one Action
    """
    push_button(action)


def replay_sequence(sequence: Sequence):
    """
    Replay sequence

    :param sequence: sequence to replay
    """
    for action in sequence:
        replay_action(action)
