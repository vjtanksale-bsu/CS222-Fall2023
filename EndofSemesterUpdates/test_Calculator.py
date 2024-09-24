# test_calculator.py - Unit tests for the Calculator class

import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the Calculator object before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method of the Calculator class."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        """Test the subtract method of the Calculator class."""
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        """Test the multiply method of the Calculator class."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_divide(self):
        """Test the divide method of the Calculator class."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
