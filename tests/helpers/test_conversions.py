from tests.utilities.base_testbase import TestCase
from tests.utilities.base_testrunner import TestRunner
from tests.utilities.formatting_utils import arg_detailed

from helpers.conversion import convert_to_ml, parse_size_token
from helpers.units import Unit


def convert_to_ml_wrapper(raw: str):
    parts = raw.lower().strip().split()

    if len(parts) != 2:
        return None

    number_str, unit_str = parts
    number = float(number_str)

    unit = Unit.from_symbol(unit_str)
    if unit is None:
        return None

    return convert_to_ml(number, unit)


def test_convert_to_ml():
    cases = [
        TestCase("750 ml", 750),
        TestCase("1.75 l", 1750),
        TestCase("1 floz", 30),
        TestCase("10 cl", 100),
    ]

    runner = TestRunner(detailed=arg_detailed())
    runner.run(convert_to_ml_wrapper, cases, title="convert_to_ml Test Suite")


def test_parse_size_token():
    cases = [
        TestCase("750ml", 750),
        TestCase("1.75l", 1750),
        TestCase("100 ml", 100),
        TestCase("50 floz", convert_to_ml(50, Unit.FLOZ)),
        TestCase("10 cl", 100),
        TestCase("not_a_size", None),
    ]

    runner = TestRunner(detailed=arg_detailed())
    runner.run(parse_size_token, cases, title="parse_size_token Test Suite")


if __name__ == "__main__":
    test_convert_to_ml()
    test_parse_size_token()
