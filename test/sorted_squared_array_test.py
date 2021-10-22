import unittest
from Arrays import sorted_squared_array

class TestSortedSquaredArray(unittest.TestCase):
    def test_sorted_squared_array(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sorted_squared_array.sortedSquaredArray(array)
        self.assertEqual(expected, actual)
        
    def test_sorted_squared_array_2(self):
        array = [1]
        expected = [1]
        actual = sorted_squared_array.sortedSquaredArray(array)
        self.assertEqual(expected, actual)

    def test_sorted_squared_array_3(self):
        array = [1, 2]
        expected = [1, 4]
        actual = sorted_squared_array.sortedSquaredArray(array)
        self.assertEqual(expected, actual)

    def test_sorted_squared_array_4(self):
        array = [-3, -2, -1]
        expected = [1, 4, 9]
        actual = sorted_squared_array.sortedSquaredArray(array)
        self.assertEqual(expected, actual)

    def test_sorted_squared_array_5(self):
        array = [-10, -5, 0, 5, 10]
        expected = [0, 25, 25, 100, 100]
        actual = sorted_squared_array.sortedSquaredArray(array)
        self.assertEqual(expected, actual)
