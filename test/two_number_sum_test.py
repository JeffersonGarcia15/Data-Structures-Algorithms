import unittest
from Arrays import two_number_sum


class TestTwoNumberSum(unittest.TestCase):
    def test_two_number_sum(self):
        result = two_number_sum.twoNumberSum([4, 6, 1, -3], 3)
        self.assertTrue(len(result))
        self.assertTrue(6 in result)
        self.assertTrue(-3 in result)
        self.assertTrue(result == [6, -3] or result == [-3, 6])

    def test_two_number_sum_2(self):
        result = two_number_sum.twoNumberSum([4, 6, 1], 5)
        self.assertTrue(len(result))
        self.assertTrue(4 in result)
        self.assertTrue(1 in result)
        self.assertTrue(result == [4, 1] or result == [1, 4])

    def test_two_number_sum_3(self):
        result = two_number_sum.twoNumberSum(
            [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163)
        self.assertTrue(len(result))
        self.assertTrue(-47 in result)
        self.assertTrue(210 in result)
        self.assertTrue(result == [-47, 210] or result == [210, -47])

    def test_two_number_sum_first_non_possible_sum(self):
        result = two_number_sum.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15)
        self.assertEqual(result, [])

    def test_two_number_sum_no_possible_sum(self):
        result = two_number_sum.twoNumberSum([14], 15)
        self.assertEqual(result, [])

    def test_two_number_sum_possible_sum_but_no_two_numbers(self):
        result = two_number_sum.twoNumberSum([15], 15)
        self.assertEqual(result, [])
