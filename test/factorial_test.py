import unittest
import timeout_decorator
from Recursion import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        result = factorial.factorial(1)
        self.assertTrue(result == 1)

    def test_factorial_2(self):
        result = factorial.factorial(2)
        self.assertTrue(result == 2)

    def test_factorial_3(self):
        result = factorial.factorial(5)
        self.assertTrue(result == 120)

    def test_factorial_4(self):
        result = factorial.factorial(10)
        self.assertTrue(result == 3628800)
