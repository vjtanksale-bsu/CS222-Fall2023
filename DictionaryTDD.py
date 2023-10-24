import unittest
class MyDictionary():
    def __init__(self):
        self.dict = {}
    def get(self, k):
        return self.dict.get(k)
    def add(self, k, v):
        self.dict[k] = v
class TestMyDictionary(unittest.TestCase):
    def setUp(self):
        self.myDictionary = MyDictionary()
    def test_add(self):
        self.myDictionary.add('000', 'Alice')
        self.assertEqual(self.myDictionary.get('000'), 'Alice')
    def test_getExistingKey(self):
        self.myDictionary.add('001','Bob')
        result = self.myDictionary.get('001')
        self.assertEqual(result, 'Bob')
    def test_getNonExistentKey(self):
        result = self.myDictionary.get('002')
        self.assertIsNone(result)
if __name__ == "__main__":
    unittest.main()