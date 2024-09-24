# test_utils.py - Unit tests for the Utils class

import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    
    def test_multiply(self):
        """Test the static multiply method."""
        result = Utils.multiply(3, 4)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
