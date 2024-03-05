"""
Base action module
"""
from pydantic import BaseModel, ConfigDict


class Action(BaseModel):
    """
    Action model
    """
    model_config = ConfigDict(frozen=True)
    subtype: str = 'Action'
