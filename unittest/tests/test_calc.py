# import unittest
# # import sys
# # sys.path.append(
# #     'unittest/problems')

# from unittest.calc import add
# # import problems.calc
# # from problems import calc

# class TestCalc(unittest.TestCase):
#     def test_add(self):
#         result = calc.add(10, 5)
#         self.assertEqual(result, 15)
        
import unittest 
from problems import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


