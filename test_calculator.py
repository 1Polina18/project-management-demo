# test_calculator.py

import unittest
from calculator.calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()