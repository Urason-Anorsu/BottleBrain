from tests.utilities.base_testbase import TestCase
from tests.utilities.base_testrunner import TestRunner
from tests.utilities.formatting_utils import arg_detailed

from helpers.units import Unit


def test_unit_from_symbol():
    cases = [
        TestCase("ml", Unit.ML),
        TestCase("ML", Unit.ML),
        TestCase("l", Unit.LITER),
        TestCase("L", Unit.LITER),
        TestCase("floz", Unit.FLOZ),
        TestCase("FLOZ", Unit.FLOZ),
        TestCase("cl", Unit.CL),
        TestCase("CL", Unit.CL),
        TestCase("unknown", None),
        TestCase("", None),
    ]

    runner = TestRunner(detailed=arg_detailed())
    runner.run(Unit.from_symbol, cases, title="Unit.from_symbol Test Suite")


def test_unit_multipliers():
    cases = [
        TestCase("ml", 1.0),
        TestCase("l", 1000.0),
        TestCase("floz", 29.5735),
        TestCase("cl", 10.0),
    ]

    def resolve_multiplier(raw: str):
        unit = Unit.from_symbol(raw)
        if unit is None:
            return None
        return unit.multiplier

    runner = TestRunner(detailed=arg_detailed())
    runner.run(resolve_multiplier, cases, title="Unit Multiplier Test Suite")


if __name__ == "__main__":
    test_unit_from_symbol()
    test_unit_multipliers()
