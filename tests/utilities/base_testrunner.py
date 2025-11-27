import shutil
from .formatting_utils import Color, diff_output
from .base_testbase import TestCase
from typing import Any, List

class TestRunner:
    def __init__(self, detailed: bool = False):
        self.detailed = detailed
        self.passed = 0
        self.failed = 0

    def print_header(self, title: str):
        width = shutil.get_terminal_size((80, 20)).columns
        print("\n" + Color.CYAN.value + "═" * width + Color.RESET.value)
        print(Color.CYAN.value + title.center(width) + Color.RESET.value)
        print(Color.CYAN.value + "═" * width + Color.RESET.value + "\n")

    def success(self, case: TestCase, result: Any):
        print(f"{Color.GREEN.value}✓{Color.RESET.value} {case.label}")
        if self.detailed:
            print(f"    {Color.CYAN.value}Output:  {Color.RESET.value}{result}")
            print(f"    {Color.CYAN.value}Expected:{Color.RESET.value}{case.expected}\n")
        self.passed += 1

    def failure(self, case: TestCase, result: Any):
        print(f"{Color.RED.value}FAILED:{Color.RESET.value} {case.label}")
        print(f"    {Color.YELLOW.value}Output:  {Color.RESET.value}{result}")
        print(f"    {Color.YELLOW.value}Expected:{Color.RESET.value}{case.expected}")

        diff = diff_output(result, case.expected)
        if diff:
            print("\nDiff:")
            print(diff)

        self.failed += 1

    def run(self, func, cases: List[TestCase], title="Test Suite"):
        self.print_header(title)

        for case in cases:
            result = func(case.raw)

            if result == case.expected:
                self.success(case, result)
            else:
                self.failure(case, result)

        self.summary()

    def summary(self):
        print()
        print(f"{Color.GREEN.value}{self.passed} passed{Color.RESET.value}, "
              f"{Color.RED.value}{self.failed} failed{Color.RESET.value}")

        if self.failed == 0:
            print(f"\n{Color.GREEN.value}All tests passed{Color.RESET.value}\n")
        else:
            print(f"\n{Color.RED.value}Some tests failed{Color.RESET.value}\n")