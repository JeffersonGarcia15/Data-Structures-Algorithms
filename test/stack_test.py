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
        self.assertEqual(self.first == self.stack.first and self.last == self.stack.last, True)
        
    
