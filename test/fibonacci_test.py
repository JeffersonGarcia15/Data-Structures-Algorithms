import unittest
import timeout_decorator
from Recursion import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        result = fibonacci.fibonacci(2)
        self.assertTrue(result == 1)

    def test_fibonacci_2(self):
        result = fibonacci.fibonacci(3)
        self.assertTrue(result == 2)

    def test_fibonacci_3(self):
        result = fibonacci.fibonacci(6)
        self.assertTrue(result == 8)

    def test_fibonacci_4(self):
        result = fibonacci.fibonacci(9)
        self.assertTrue(result == 34)

    def test_fibonacci_5(self):
        result = fibonacci.fibonacci(25)
        self.assertTrue(result == 75025)

    def test_fibonacci_5(self):
        result = fibonacci.fibonacci(25)
        self.assertTrue(result == 75025)

    @timeout_decorator.timeout(5)
    def test_fibonacci_first_solution_that_breaks_if_solution_is_too_slow(self):
        result = fibonacci.fibonacci(40)
        self.assertTrue(result == 102334155)

    @timeout_decorator.timeout(5)
    def test_fibonacci_second_solution_that_breaks_if_solution_is_too_slow(self):
        result = fibonacci.fibonacci(50)
        self.assertTrue(result == 12586269025)

    @timeout_decorator.timeout(5)
    def test_fibonacci_third_solution_that_breaks_if_solution_is_too_slow(self):
        result = fibonacci.fibonacci(45)
        self.assertTrue(result == 1134903170)

    @timeout_decorator.timeout(5)
    def test_fibonacci_third_solution_that_breaks_if_solution_is_too_slow(self):
        result = fibonacci.fibonacci(100)
        self.assertTrue(result == 354224848179261915075)
