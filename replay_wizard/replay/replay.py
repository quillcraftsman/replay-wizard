"""
Replay core module
"""
import time
from replay_wizard.models import Action
from .keyboard import push_button


def replay_action(action: Action):
    """
    Replay one Action
    """
    push_button(action)


def replay_simple_sequence(sequence):
    """
    Just repeat all actions

    :param sequence: current sequence
    """
    for action in sequence:
        replay_action(action)


def create_timedelta_list(timestamp_list):
    """
    Create timedelta list

    :param timestamp_list: List with timedelta
    """
    timedelta_list = [0]
    for i in range(1, len(timestamp_list)):
        value = timestamp_list[i] - timestamp_list[i-1]
        timedelta_list.append(value)

    return timedelta_list


def replay_time_sequence(sequence):
    """
    Replay sequence with time

    :param sequence: current sequence
    """
    timedelta_list = create_timedelta_list(sequence.timestamp_list)
    for action, delay in zip(sequence.actions, timedelta_list):
        time.sleep(delay)
        replay_action(action)


def replay(sequence, true_time=False):
    """
    Replay sequence

    :param sequence: sequence to replay
    :param true_time: replay or not sequence with true time. default = False
    """
    if true_time:
        replay_time_sequence(sequence)
    else:
        replay_simple_sequence(sequence)