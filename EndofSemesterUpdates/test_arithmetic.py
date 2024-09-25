import unittest
from arithmetic import add_and_subtract
class TestAddAndSubtract(unittest.TestCase):
    def test_add_and_subtract(self):
        # Test case 1: Positive integers
        result = add_and_subtract(10, 5)
        self.assertEqual(result, (15, 5))  # Expected result: (15, 5)
       
        # Test case 2: Negative integers
        result = add_and_subtract(-10, -5)
        self.assertEqual(result, (-15, -5))  # Expected result: (-15, -5)
       
        # Test case 3: Mixed positive and negative integers
        result = add_and_subtract(10, -5)
        self.assertEqual(result, (5, 15))  # Expected result: (5, 15)
       
        # Test case 4: Zero values
        result = add_and_subtract(0, 0)
        self.assertEqual(result, (0, 0))  # Expected result: (0, 0)

if __name__ == '__main__':
    unittest.main()