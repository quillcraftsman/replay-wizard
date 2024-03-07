"""
App CLI module
"""
import time
from replay_wizard import capture
from replay_wizard.storage import save_to_file
from .parser import get_parser, add_arguments


def capture_cli():
    """
    Run capture CLI wizard-capture
    """

    parser = get_parser('wizard-capture')
    parser = add_arguments(parser)

    args = parser.parse_args()

    sequence_name = args.sequence
    delay = args.delay
    keyboard = args.keyboard
    mouse = args.mouse

    time.sleep(delay)

    sequence = capture(sequence_name, keyboard=keyboard, mouse=mouse)
    save_to_file(sequence)
