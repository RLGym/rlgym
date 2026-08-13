"""
An RLGym renderer.
"""
from abc import abstractmethod, ABC
from typing import Any, Dict, Generic
from ..typing import StateType


class Renderer(ABC, Generic[StateType]):
    """
    The renderer class. This class is responsible for rendering a state.
    """

    @abstractmethod
    def render(self, state: StateType, shared_info: Dict[str, Any]) -> Any:
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError
