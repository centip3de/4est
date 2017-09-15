import unittest
from forest.stack import Stack
from forest.interp.operators import SwapOP, ClearStackOP, PopOP, DupOP

class StackOperatorTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack([1, 2])

    def test_swap_op(self):
        out = SwapOP.invoke(None, None, self.stack)
        out[0] == None
        out[1].mem == [2, 1]

    def test_clear_stack_op(self):
        out = ClearStackOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [])

    def test_pop_op(self):
        out = PopOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [1])

    def test_dup_op(self):
        out = DupOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [1, 2, 2])
