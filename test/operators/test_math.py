import unittest

from forest.interp.operators import AddOP, SubOP, DivOP, ModOP, MulOP, IncOP, DecOP

class MathOperatorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_dec_op(self):
        assert(DecOP.invoke(1, None, []) == 0)

    def test_inc_op(self):
        assert(IncOP.invoke(1, None, []) == 2)

    def test_add_op(self):
        assert(AddOP.invoke(1, 1, []) == 2)

    def test_sub_op(self):
        assert(SubOP.invoke(1, 2, []) == -1)

    def test_div_op(self):
        assert(DivOP.invoke(2, 4, []) == 2)

    def test_mul_op(self):
        assert(MulOP.invoke(2, 4, []) == 8)
