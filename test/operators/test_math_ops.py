import unittest

from forest.interp.operators import AddOP, SubOP, DivOP, ModOP, MulOP, IncOP, DecOP, ExpOP, LtOP, GtOP

class MathOperatorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_dec_op(self):
        assert(DecOP.invoke(1, None, []) == (0, []))

    def test_inc_op(self):
        assert(IncOP.invoke(1, None, []) == (2, []))

    def test_add_op(self):
        assert(AddOP.invoke(1, 1, []) == (2, []))

    def test_sub_op(self):
        assert(SubOP.invoke(1, 2, []) == (-1, []))

    def test_div_op(self):
        assert(DivOP.invoke(2, 4, []) == (0.5, []))

    def test_mul_op(self):
        assert(MulOP.invoke(2, 4, []) == (8, []))

    def test_exp_op(self):
        assert(ExpOP.invoke(2, 4, []) == (2**4, []))

    def test_lt_op(self):
        assert(LtOP.invoke(2, 4, []) == (True, []))

    def test_gt_op(self):
        assert(GtOP.invoke(2, 4, []) == (False, []))
