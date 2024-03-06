"""
App CLI module
"""
import time
import argparse
from replay_wizard import capture
from replay_wizard.storage import save_to_file
from .parser import str2bool


def capture_cli():
    """
    Run capture CLI wizard-capture
    """

    program_description = """
         ReplayWizard is a powerful automation tool designed to streamline your workflow by capturing 
         and replaying your interactions with your computer
    """

    parser = argparse.ArgumentParser(
        prog='wizard-capture',
        description=program_description,
        epilog='Use wizard-capture -h to get help'
    )

    parser.add_argument('sequence')
    parser.add_argument('-d', '--delay', default=0, type=int)
    parser.add_argument('-t', '--timedelta', default=False, type=str2bool)
    parser.add_argument('-k', '--keyboard', default=True, type=str2bool)
    parser.add_argument('-mo', '--mouse', default=False, type=str2bool)
    args = parser.parse_args()

    sequence_name = args.sequence
    delay = args.delay
    timedelta = args.timedelta
    keyboard = args.keyboard
    mouse = args.mouse

    time.sleep(delay)

    print(capture)
    print(type(capture))
    sequence = capture(sequence_name, timedelta, keyboard=keyboard, mouse=mouse)
    save_to_file(sequence)
