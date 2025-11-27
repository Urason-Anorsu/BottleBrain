from enum import Enum
from typing import Optional


class Unit(Enum):
    ML    = ("ml",    1.0)
    LITER = ("l",     1000.0)
    FLOZ  = ("floz",  29.5735)
    CL    = ("cl",    10.0)

    def __init__(self, symbol: str, multiplier: float):
        self.symbol = symbol
        self.multiplier = multiplier

    @classmethod
    def from_symbol(cls, s: str) -> Optional["Unit"]:
        normalized = s.lower().strip()

        _LOOKUP = {unit.symbol: unit for unit in cls}

        return _LOOKUP.get(normalized)

