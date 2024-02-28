"""
Sequence module
"""
from typing import List
from pydantic import BaseModel
from .action import Action


class Sequence(BaseModel):
    """
    Action sequence
    """
    name: str
    actions: List[Action] = []

    def __len__(self):
        return len(self.actions)

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
