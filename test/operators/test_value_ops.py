import unittest
from forest.interp.operators import TruthOP, FalseOP, IntOP, StringOP, EmptyListOP

class ValueOperatorsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_truth(self):
        assert(TruthOP.invoke(None, None, []) == (True, []))

    def test_false(self):
        assert(FalseOP.invoke(None, None, []) == (False, []))

    def test_int(self):
        assert(IntOP.invoke("8", None, []) == (8, []))

    def test_string(self):
        assert(StringOP.invoke(8, None, []) == ("8", []))

    def test_list(self):
        assert(EmptyListOP.invoke(None, None, []) == ([], []))
