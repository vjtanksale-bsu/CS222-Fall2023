import unittest
from ooslugifier import Slugifier  # Importing the Slugifier class

class TestSlugifier(unittest.TestCase):
    
    def setUp(self):
        self.slugifier = Slugifier()  # Create a new instance for each test

    def test_slugify_basic(self):
        self.assertEqual(self.slugifier.slugify("Hello World"), "hello-world")
    
    def test_slugify_with_punctuation(self):
        self.assertEqual(self.slugifier.slugify("Python is the best!"), "python-is-the-best")
    
    def test_slugify_with_multiple_spaces(self):
        self.assertEqual(self.slugifier.slugify("   Python   is   awesome  "), "python-is-awesome")
    
    #def test_slugify_special_characters(self):
    #    self.assertEqual(self.slugifier.slugify("C# & Python: A Comparison!"), "c-and-python-a-comparison")

    def test_slugify_empty_string(self):
        self.assertEqual(self.slugifier.slugify(""), "")
    
    def test_slugify_only_special_characters(self):
        self.assertEqual(self.slugifier.slugify("@#$%^&"), "")
    
    def test_custom_replacement_character(self):
        custom_slugifier = Slugifier(replacement_char='_')
        self.assertEqual(custom_slugifier.slugify("Hello World"), "hello_world")

if __name__ == '__main__':
    unittest.main()
