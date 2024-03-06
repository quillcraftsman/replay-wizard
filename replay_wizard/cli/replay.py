"""
App CLI module
"""
import time
import argparse
from replay_wizard import capture, replay
from replay_wizard.storage import save_to_file, load_from_file
from .parser import str2bool


def replay_cli():
    """
    Run replay CLI wizard-replay
    """

    program_description = """
         ReplayWizard is a powerful automation tool designed to streamline your workflow by capturing 
         and replaying your interactions with your computer
    """

    parser = argparse.ArgumentParser(
        prog='wizard-repaly',
        description=program_description,
        epilog='Use wizard-replay -h to get help'
    )

    parser.add_argument('sequence')
    parser.add_argument('-d', '--delay', default=0, type=int)
    parser.add_argument('-t', '--timedelta', default=False, type=str2bool)
    parser.add_argument('-m', '--monitoring', default=False, type=str2bool)
    parser.add_argument('-k', '--keyboard', default=True, type=str2bool)
    parser.add_argument('-mo', '--mouse', default=False, type=str2bool)
    args = parser.parse_args()

    sequence_name = args.sequence
    delay = args.delay
    timedelta = args.timedelta
    is_monitoring = args.monitoring
    keyboard = args.keyboard
    mouse = args.mouse

    time.sleep(delay)

    sequence = load_from_file(sequence_name, true_time=timedelta)
    # create duplicated monitoring sequence in monitoring mode
    # to check how sequence will be replayed
    if is_monitoring:
        duplicated_sequence = capture(
            'monitoring',
            timedelta,
            non_blocking_mode=True,
            keyboard=keyboard,
            mouse=mouse
        )
    replay(sequence, timedelta)

    if is_monitoring:
        save_to_file(duplicated_sequence)
