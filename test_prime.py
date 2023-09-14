import unittest
from primenumber import IsPrime
class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(IsPrime(2))
    def test_three(self):
        self.assertTrue(IsPrime(3))
    def test_fifteen(self):
        self.assertFalse(IsPrime(15))
if __name__ == '__main__':
    unittest.main()