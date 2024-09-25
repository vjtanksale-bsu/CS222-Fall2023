from maxmin import max_and_min
import unittest

class TestMaxAndMin(unittest.TestCase):
    def test_max_and_min(self):
        # Test case 1: List of positive numbers
        result = max_and_min([1, 2, 3, 4, 5])
        self.assertEqual(result, (5, 1))  # Expected result: (max=5, min=1)

        # Test case 2: List with negative numbers
        result = max_and_min([-10, -5, 0, 5, 10])
        self.assertEqual(result, (10, -10))  # Expected result: (max=10, min=-10)

        # Test case 3: List with all same numbers
        result = max_and_min([7, 7, 7, 7])
        self.assertEqual(result, (7, 7))  # Expected result: (max=7, min=7)

        # Test case 4: List with a single element
        result = max_and_min([42])
        self.assertEqual(result, (42, 42))  # Expected result: (42, 42)

if __name__ == '__main__':
    unittest.main()