import unittest
from weather import CAAlert
class WeatherTest(unittest.TestCase):
    def test_CAAlert(self):
        self.assertEqual(CAAlert(), "Excessive Heat Warning")

if __name__ == '__main__':
    unittest.main()