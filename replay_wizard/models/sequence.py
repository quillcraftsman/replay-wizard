"""
Sequence module
"""
import time
from typing import List
from pydantic import BaseModel, ConfigDict
from .action import Action


class Sequence(BaseModel):
    """
    Action sequence
    """
    model_config = ConfigDict(frozen=True)

    name: str
    actions: List[Action] = []
    # true_time: bool = False

    def __len__(self):
        return len(self.actions)

    def __iter__(self):
        return iter(self.actions)

    def add(self, new_action: Action):
        """
        Add action to sequence

        :param new_action: Action to add
        :return: None
        """
        self.actions.append(new_action)

    def __contains__(self, item):
        """
        in method
        """
        return item in self.actions


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


def get_sequence(true_time=False) -> Sequence:
    """
    Fabric method to get sequence object

    :param true_time: use true time
    """
    return TimeSequence if true_time else Sequence
