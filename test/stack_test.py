import unittest
from data_structures import stack

class Test(unittest.TestCase):
    def setUp(self):
        self.node = stack.Node(1)
        self.stack = stack.Stack()
        
    def tearDown(self):
        while not self.stack.size == 0:
            self.stack.pop()
            
    def test_that_pointers_are_at_null_in_empty_stack(self):
        self.first = None
        self.last = None
        self.assertEqual(self.first, self.stack.first)
        self.assertEqual(self.last, self.stack.last)
        
    def test_that_pointers_are_at_the_only_value_in_stack(self):
        self.stack.push(10)
        self.first = 10
        self.last = 10
        self.assertEqual(self.first, self.stack.first.value)
        self.assertEqual(self.last, self.stack.last.value)

    def test_that_pointers_are_successfully_relocated_when_having_more_than_one_value(self):
        self.stack.push(10)
        self.stack.push(20)
        self.first = 20
        self.last = 10
        self.assertEqual(self.first, self.stack.first.value)
        self.assertEqual(self.last, self.stack.last.value)
        
    def test_that_checks_if_can_do_pop_on_empty_stack(self):
        self.stack.pop()
        self.first = None
        self.last = None
        self.assertEqual(self.first, self.stack.first)
        self.assertEqual(self.last, self.stack.last)

    def test_that_checks_if_pop_moves_pointer_to_none_on_stack_with_a_single_value(self):
        self.stack.push(1)
        self.stack.pop()
        self.first = None
        self.last = None
        self.assertEqual(self.first, self.stack.first)
        self.assertEqual(self.last, self.stack.last)
        
    def test_that_checks_if_pop_moves_pointer_to_same_node_on_stack_with_two_values(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.first = 1
        self.last = 1
        self.assertEqual(self.first, self.stack.first.value)
        self.assertEqual(self.last, self.stack.last.value)
