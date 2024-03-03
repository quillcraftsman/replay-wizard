"""
App CLI module
"""
import time
import argparse
from replay_wizard import capture, replay
from replay_wizard.storage import save_to_file, load_from_file

CAPTURE = 'capture'
REPLAY = 'replay'


def run_cli():
    """
    Run CLI
    """

    program_description = """
         ReplayWizard is a powerful automation tool designed to streamline your workflow by capturing 
         and replaying your interactions with your computer
    """

    parser = argparse.ArgumentParser(
        prog='replay-wizard',
        description=program_description,
        epilog='Use replay-wizard -h to get help'
    )

    parser.add_argument('mode', choices=[CAPTURE, REPLAY])  # positional argument
    parser.add_argument('sequence')
    parser.add_argument('-d', '--delay', default=0, type=int)
    parser.add_argument('-t', '--timedelta', default=False, type=bool)
    parser.add_argument('-m', '--monitoring', default=False, type=bool)
    args = parser.parse_args()

    sequence_name = args.sequence
    mode = args.mode
    delay = args.delay
    timedelta = args.timedelta
    is_monitoring = args.monitoring

    time.sleep(delay)

    if mode == CAPTURE:
        sequence = capture(sequence_name, timedelta)
        save_to_file(sequence)
    else:
        sequence = load_from_file(sequence_name, true_time=timedelta)
        # create duplicated monitoring sequence in monitoring mode
        # to check how sequence will be replayed
        if is_monitoring:
            duplicated_sequence = capture('monitoring', timedelta, non_blocking_mode=True)
        replay(sequence, timedelta)

        if is_monitoring:
            save_to_file(duplicated_sequence)
