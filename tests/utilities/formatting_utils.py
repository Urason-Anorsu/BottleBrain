import os
import sys
from enum import Enum
from typing import Any

class Color(Enum):
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def diff_output(result: Any, expected: Any) -> str:
    if not isinstance(result, list) or not isinstance(expected, list):
        return ""

    diff = []
    for r, e in zip(result, expected):
        if r == e:
            diff.append(f"  {r}")
        else:
            diff.append(f"{Color.RED.value}- {r}{Color.RESET.value}")
            diff.append(f"{Color.GREEN.value}+ {e}{Color.RESET.value}")

    if len(result) > len(expected):
        for r in result[len(expected):]:
            diff.append(f"{Color.RED.value}- {r}{Color.RESET.value}")
    elif len(expected) > len(result):
        for e in expected[len(result):]:
            diff.append(f"{Color.GREEN.value}+ {e}{Color.RESET.value}")

    return "\n".join(diff)

def arg_detailed() -> bool:
    return "--detailed" in sys.argv or "-d" in sys.argv
