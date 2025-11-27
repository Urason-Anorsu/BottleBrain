from tests.helpers.test_units import test_unit_from_symbol, test_unit_multipliers
from tests.helpers.test_conversions import test_convert_to_ml, test_parse_size_token
from tests.test_tokenizer import test_basic_tokenize


TESTS = {
    "Unit.from_symbol": test_unit_from_symbol,
    "Unit.multipliers": test_unit_multipliers,
    "convert_to_ml": test_convert_to_ml,
    "parse_size_token": test_parse_size_token,
    "basic_tokenize": test_basic_tokenize,
}


def list_all_tests():
    return sorted(TESTS.keys())

def run_single(name: str):
    TESTS[name]()