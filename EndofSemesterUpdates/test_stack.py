import unittest
from stack import Stack  # Import the Stack class

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])
        self.stack.push(2)
        self.assertEqual(self.stack.items, [1, 2])

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

if __name__ == '__main__':
    unittest.main()