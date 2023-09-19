import unittest
from Assignment1 import SumofOdd, Tuition
class Assignment1(unittest.TestCase):
    def test_SumofOdd(self):
        self.assertEqual(SumofOdd(3, 8), 15)
    def test_Tuition(self):
        self.assertEqual(Tuition(5), 9274.19)
if __name__ == '__main__':
    unittest.main()