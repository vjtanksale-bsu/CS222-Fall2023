import unittest
from calculator import Calculator
class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(5, 3)
    
    def test_sum(self):
        #calculator = Calculator(5, 3)
        self.assertEqual(self.calculator.GetSum(), 8, 'The answer is incorrect.')        
    def test_difference(self):
        #calculator = Calculator(4, 10)
        self.assertEqual(self.calculator.GetDifference(), 2, "The answer is incorrect")
    def test_quotient(self):
        self.assertEqual(self.calculator.GetQuotient(), 5/3, "The answer is incorrect")
if __name__ == '__main__':
    unittest.main()