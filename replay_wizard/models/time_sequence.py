"""
Time sequence model
"""
import time
from .sequence import Sequence
from .action import Action


class TimeSequence(Sequence):
    """
    Sequence with time
    """
    timestamp_list: list = []

    @staticmethod
    def get_current_timestamp():
        """
        Get current timestamp
        """
        return time.time()

    def add(self, new_action: Action):
        super().add(new_action)
        timestamp = self.get_current_timestamp()
        self.timestamp_list.append(timestamp)

    # def is_valid_timestamps(self):
    #     """
    #     Correct timestamp list
    #     """
    #     return len(self.timestamp_list) == len(self.actions)
