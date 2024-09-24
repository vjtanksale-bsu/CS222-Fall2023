# test_employee.py - Unit tests for the Employee class

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        """Set up an Employee object for testing."""
        self.employee = Employee("John", "Doe", 50000)

    def test_give_raise(self):
        """Test the give_raise method."""
        self.employee.give_raise(5000)
        self.assertEqual(self.employee.salary, 55000)


if __name__ == '__main__':
    unittest.main()
