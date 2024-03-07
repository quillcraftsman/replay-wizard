"""
App CLI module
"""
import time
from replay_wizard import capture, replay
from replay_wizard.storage import save_to_file, load_from_file
from .parser import str2bool, get_parser, add_arguments


def replay_cli():
    """
    Run replay CLI wizard-replay
    """

    parser = get_parser('wizard-replay')
    parser = add_arguments(parser)
    parser.add_argument('-t', '--timedelta', default=False, type=str2bool)
    parser.add_argument('-m', '--monitoring', default=False, type=str2bool)

    args = parser.parse_args()

    sequence_name = args.sequence
    delay = args.delay
    timedelta = args.timedelta
    is_monitoring = args.monitoring
    keyboard = args.keyboard
    mouse = args.mouse

    time.sleep(delay)

    sequence = load_from_file(sequence_name)
    # create duplicated monitoring sequence in monitoring mode
    # to check how sequence will be replayed
    if is_monitoring:
        duplicated_sequence = capture(
            'monitoring',
            non_blocking_mode=True,
            keyboard=keyboard,
            mouse=mouse
        )
    replay(sequence, timedelta)

    if is_monitoring:
        save_to_file(duplicated_sequence)
