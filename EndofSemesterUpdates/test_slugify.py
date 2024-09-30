import unittest
from slugify import slugify  # Importing the slugify function

class TestSlugifyFunction(unittest.TestCase):

    def test_slugify_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    
    def test_slugify_with_punctuation(self):
        self.assertEqual(slugify("Python is the best!"), "python-is-the-best")
    
    def test_slugify_with_multiple_spaces(self):
        self.assertEqual(slugify("   Python   is   awesome  "), "python-is-awesome")
    
    #def test_slugify_special_characters(self):
    #    self.assertEqual(slugify("C# & Python: A Comparison!"), "c-and-python-a-comparison")

    def test_slugify_empty_string(self):
        self.assertEqual(slugify(""), "")
    
    def test_slugify_only_special_characters(self):
        self.assertEqual(slugify("@#$%^&"), "")

if __name__ == '__main__':
    unittest.main()
