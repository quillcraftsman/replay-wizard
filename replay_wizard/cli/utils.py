"""
Useful commands
"""
import os
from .parser import get_only_parser


def is_sequence_file(filename, extension, isfile):
    """
    Is sequence file

    :param filename: filename
    :param extension: file extension
    """
    return filename.endswith(f'.{extension}') and isfile(filename)


def show_sequences(all_files, extension, isfile, show=print):
    """
    Show sequence

    :param all_files: files to check
    :param extension: sequence file extension
    :param isfile: function to check not dir
    :param show: show function, default print
    """
    for file in [file for file in all_files if is_sequence_file(file, extension, isfile)]:
        show(file)


def sequence_list_cli():
    """
    Get sequence list
    """
    parser = get_only_parser('wizard-list')
    parser.add_argument('-e', '--extension', default='sequence', type=str)

    args = parser.parse_args()

    extension = args.extension

    show_sequences(os.listdir(), extension, os.path.isfile, print)
