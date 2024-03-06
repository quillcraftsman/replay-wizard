"""
Sequence module
"""
from pydantic import BaseModel, ConfigDict
from replay_wizard.models.utils import get_action


class Sequence(BaseModel):
    """
    Action sequence
    """
    model_config = ConfigDict(frozen=True)

    name: str
    actions: list = []

    @classmethod
    def model_validate(cls, *args, **kwargs):
        result = super(Sequence, cls).model_validate(
            *args, **kwargs
        )
        for i, action in enumerate(result):
            subtype = action['subtype']
            action_cls = get_action(subtype)
            result.actions[i] = action_cls(**action)

        return result

    def update(self, other):
        """
        Update method

        :param other: other sequence
        """
        self.actions.extend(other.actions)

    def __len__(self):
        return len(self.actions)

    def __iter__(self):
        return iter(self.actions)

    def add(self, new_action):
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

    def __getitem__(self, item):
        return self.actions[item]

    @classmethod
    def combine(cls, name, *sequences):
        """
        Combine many sequences to one
        """
        result = cls(name=name)
        for sequence in sequences:
            result.update(sequence)
        return result
