"""
Replay core module
"""
import time
from .utils import get_replayer


def replay_action(action):
    """
    Replay one Action
    """
    replayer = get_replayer(action.subtype)
    replayer(action)


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


def one_thread_sleep_strategy(sequence):
    """
    Calculate timedelta between actions.
    Run action then sleep

    :param sequence: current sequence
    """
    timedelta_list = create_timedelta_list(sequence.timestamp_list)
    for action, delay in zip(sequence.actions, timedelta_list):
        time.sleep(delay)
        replay_action(action)


def schedule_strategy(sequence):
    """
    Thirst create schedule
    Then try to run action by schedule in cycle

    :param sequence: current sequence
    """
    if len(sequence) == 0:
        return
    schedule_list = []
    old_start_time = sequence.timestamp_list[0]
    adjustment = 0.00018
    new_start_time = time.time() + adjustment
    delta_time = new_start_time - old_start_time
    for item in sequence.timestamp_list:
        new_item = item+delta_time
        schedule_list.append(new_item)

    current_action_index = 0
    schedule_list_len = len(schedule_list)
    while current_action_index < schedule_list_len:
        current_action = sequence.actions[current_action_index]
        current_schedule_point = schedule_list[current_action_index]
        current_time = time.time()
        if current_time >= current_schedule_point:
            replay_action(current_action)
            current_action_index += 1


def replay_time_sequence(sequence, strategy=schedule_strategy):
    """
    Replay sequence with time

    :param sequence: current sequence
    :param strategy: how to replay time sequence
    """
    strategy(sequence)


def replay(sequence, true_time=False, strategy=schedule_strategy):
    """
    Replay sequence

    :param sequence: sequence to replay
    :param true_time: replay or not sequence with true time. default = False
    :param strategy: how to replay time sequence
    """
    if true_time:
        replay_time_sequence(sequence, strategy)
    else:
        replay_simple_sequence(sequence)


def compare(sequence, other_sequence):
    """
    Compare two sequences
    """
    td_list = create_timedelta_list(sequence.timestamp_list)
    other_td_list = create_timedelta_list(other_sequence.timestamp_list)
    deltas = []
    for one, two in zip(td_list, other_td_list):
        deltas.append(two-one)

    return sum(deltas)/len(deltas)
