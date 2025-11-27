from .utilities.base_testbase import TestCase
from .utilities.base_testrunner import TestRunner
from .utilities.formatting_utils import arg_detailed
from data_formatting.tokenizer import basic_tokenize


def test_basic_tokenize():
    cases = [
        TestCase("White Claw Mango 12/12 CAN", ['white','claw','mango','12/12','can']),
        TestCase("JACK DANSL Fire 750ML", ['jack','dansl','fire','750ml']),
        TestCase("Tito's Handmade Vodka - 1.75L", ['titos','handmade','vodka','1.75l']),
        TestCase("REPOSADO TEQ (750 ml)", ['reposado','teq','750','ml']),
        TestCase("Smirnoff ICE 'Party Pack' 12PK", ['smirnoff','ice','party','pack','12pk']),
    ]

    runner = TestRunner(detailed=arg_detailed())
    runner.run(basic_tokenize, cases, title="Tokenizer Test Suite")


if __name__ == "__main__":
    test_basic_tokenize()
