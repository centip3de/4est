import unittest
from forest.interp.operators import JoinOP, StackToListOP
from forest.stack import Stack

class ListOperatorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_join_op(self):
        assert(JoinOP.invoke([1, 2, 3], None, []) == ("123", []))
        assert(JoinOP.invoke(" ", [1, 2, 3], []) == ("1 2 3", []))

    def test_stack_to_list_op(self):
        stack = Stack([1, 2, 3])
        assert(StackToListOP.invoke(None, None, stack) == ([1, 2, 3], stack))
