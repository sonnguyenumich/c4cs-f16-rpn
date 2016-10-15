import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("13 1 +")
        self.assertEqual(14, result)
    def test_subtract(self):
        result = rpn.calculate("101 3 -")
        self.assertEqual(98, result)
    def test_multiply(self):
        result = rpn.calculate("2 -1 *")
        self.assertEqual(-2, result)
    def test_divide(self):
        result = rpn.calculate("25 5 /")
        self.assertEqual(5, result)
    def test_exp(self):
        result = rpn.calculate("2 5 ^")
        self.assertEqual(32, result)



