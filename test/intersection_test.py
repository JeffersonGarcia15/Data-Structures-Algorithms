import unittest
import timeout_decorator
from Arrays import intersection


class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        result = intersection.intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])
        self.assertTrue(result == [2, 6] or result == [6, 2])

    def test_intersection_2(self):
        result = intersection.intersection([2, 4, 6], [4, 2])
        self.assertTrue(result == [2, 4] or result == [4, 2])

    def test_intersection_no_possible_intersection(self):
        result = intersection.intersection([0, 1, 2], [10, 11])
        self.assertEqual(result, [])

    @timeout_decorator.timeout(5)
    def test_intersection_that_will_break_if_solution_is_too_slow(self):
        a = [i for i in range(0, 50000)]
        b = [i for i in range(0, 50000)]
        result = intersection.intersection(a, b)
        self.assertEqual(result, a)
