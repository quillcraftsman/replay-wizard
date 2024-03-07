"""
Parser module
"""
import argparse

PROGRAM_DESCRIPTION = """
         ReplayWizard is a powerful automation tool designed to streamline your workflow by capturing 
         and replaying your interactions with your computer
    """


def str2bool(v):
    """
    Console bool parameter to bool python value
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    raise argparse.ArgumentTypeError('Boolean value expected.')


def get_parser(command_name):
    """
    Get argument parser
    """
    parser = argparse.ArgumentParser(
        prog=command_name,
        description=PROGRAM_DESCRIPTION,
        epilog=f'Use {command_name} -h to get help'
    )

    parser.add_argument('sequence')
    return parser


def add_arguments(parser):
    """
    Add same arguments
    """
    parser.add_argument('-d', '--delay', default=0, type=int)
    parser.add_argument('-k', '--keyboard', default=True, type=str2bool)
    parser.add_argument('-mo', '--mouse', default=True, type=str2bool)
    return parser
