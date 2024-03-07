"""
Combine CLI
"""
from replay_wizard.models import get_sequence
from replay_wizard.storage import load_from_file, save_to_file
from .parser import get_parser


def combine_cli():
    """
    Combine CLI function
    """

    parser = get_parser('wizard-combine')
    parser.add_argument('sequences', nargs='+')
    args = parser.parse_args()

    sequence_name = args.sequence
    sequence_names = args.sequences

    sequences = []
    for name in sequence_names:
        sequence = load_from_file(name)
        sequences.append(sequence)

    sequence_cls = get_sequence()
    new_sequence = sequence_cls.combine(sequence_name, *sequences)
    save_to_file(new_sequence)
