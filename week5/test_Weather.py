import unittest
from weather import CAAlert
class WeatherTest(unittest.TestCase):
    def test_CAAlert(self):
        self.assertEqual(CAAlert(), "Wind Advisory")

if __name__ == '__main__':
    unittest.main()