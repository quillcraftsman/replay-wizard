"""
App CLI module
"""
import time
import argparse
from replay_wizard import capture, replay

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
    parser.add_argument('-t', '--timedelta', default=True, type=bool)
    args = parser.parse_args()

    sequence = args.sequence
    mode = args.mode
    delay = args.delay
    timedelta = args.timedelta

    modes = {
        CAPTURE: capture,
        REPLAY: replay,
    }

    run = modes[mode]

    time.sleep(delay)
    run(sequence, true_time=timedelta)
