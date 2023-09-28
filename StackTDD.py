import unittest
class Stack():
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)   
    def push(self, arg):
        self.items.append(arg)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return IndexError("Stack is empty")
    def is_empty(self):
        return (len(self.items) == 0)
    
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(55)
        self.assertFalse(self.stack.is_empty())
    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 2)
if __name__ == "__main__":
    unittest.main()