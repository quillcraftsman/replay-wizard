"""
Time sequence model
"""
import time

from pydantic import Field

from .action import Action
from .keyboard import KeyboardAction
from .mouse import (
    MouseAction,
    ScrollAction,
    ClickAction,
)


def get_action(subtype: str):
    """
    Get Action class by subtype (classname)
    """
    action_types = [
        KeyboardAction,
        MouseAction,
        ScrollAction,
        ClickAction,
        TimeSequence,
    ]
    action_types_dict = {
        item.__name__: item
        for item in action_types
    }
    return action_types_dict[subtype]


class TimeSequence(Action):
    """
    Sequence with time
    """
    name: str
    actions: list = []
    timestamp_list: list = []
    subtype: str = 'TimeSequence'
    start_time: float = Field(default_factory=time.time)

    def __len__(self):
        return len(self.actions)

    def __iter__(self):
        return iter(self.actions)

    def __contains__(self, item):
        """
        in method
        """
        return item in self.actions

    def __getitem__(self, item):
        return self.actions[item]

    @classmethod
    def combine(cls, name, *sequences):
        """
        Combine many sequences to one
        """
        result = cls(name=name)
        for sequence in sequences:
            result.add(sequence)
        return result

    @staticmethod
    def get_current_timestamp():
        """
        Get current timestamp
        """
        return time.time()

    def add(self, new_action):
        """
        Add new action
        """
        self.actions.append(new_action)
        timestamp = self.get_current_timestamp()
        self.timestamp_list.append(timestamp)

    def update(self, other):
        """
        Update actions
        """
        self.actions.extend(other.actions)
        self.timestamp_list.extend(other.timestamp_list)

    @classmethod
    def model_validate(cls, *args, **kwargs):
        result = super(TimeSequence, cls).model_validate(
            *args, **kwargs
        )
        for i, action in enumerate(result):
            subtype = action['subtype']
            action_cls = get_action(subtype)
            # result.actions[i] = action_cls(**action)
            result.actions[i] = action_cls.model_validate(action)
        return result
