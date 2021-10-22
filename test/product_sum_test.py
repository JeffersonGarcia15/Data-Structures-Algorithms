import unittest
from Recursion import product_sum


class TestProductSum(unittest.TestCase):
    def test_product_sum(self):
       array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
       expected = 12
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)

    def test_product_sum_2(self):
       array = [1, 2, 3, 4, 5]
       expected = 15
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)

    def test_product_sum_3(self):
       array = [1, 2, [3], 4, 5]
       expected = 18
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)

    def test_product_sum_4(self):
       array = [[1, 2], 3, [4, 5]]
       expected = 27
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)

    def test_product_sum_5(self):
       array = [[[[[5]]]]]
       expected = 600
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)

    def test_product_sum_6(self):
       array = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3,
                                                                                                           [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]
       expected = 1351
       actual = product_sum.productSum(array)
       self.assertEqual(expected, actual)
