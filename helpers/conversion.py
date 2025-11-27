import re
from typing import Optional
from .units import Unit


def convert_to_ml(value: float, unit: Unit) -> int:
    ml_value = value * unit.multiplier
    return int(round(ml_value))


def parse_size_token(token: str) -> Optional[int]:
    normalized = token.lower().strip()

    match = re.match(r"^(\d+(?:\.\d+)?)(?:\s*)([a-zA-Z]+)$", normalized)
    if not match:
        return None

    number_str, unit_str = match.groups()
    number = float(number_str)

    unit = Unit.from_symbol(unit_str)
    if unit is None:
        return None

    return convert_to_ml(number, unit)
