import unittest
from forest.interp.operators import SplitOP, AddOP, MulOP

class StrinOperatorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_split_op(self):
        assert(SplitOP.invoke("asdf asdf", " ", []) == (["asdf", "asdf"], []))

    def test_add_op(self):
        assert(AddOP.invoke("a", "b", []) == ("ab", []))

    def test_mul_op(self):
        assert(MulOP.invoke("a", 3, []) == ("aaa", []))
