from dataclasses import dataclass

from .utils import auto_init_slots


@auto_init_slots
@dataclass(slots=True, init=False)
class GameConfig:
    gravity: float
    boost_consumption: float
    dodge_deadzone: float  # TODO move to car?
