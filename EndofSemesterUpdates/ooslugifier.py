import re

class Slugifier:
    def __init__(self, replacement_char='-'):
        """
        Initialize the slugifier with an optional replacement character.
        Default is '-'.
        """
        self.replacement_char = replacement_char

    def slugify(self, text):
        # Convert the text to lowercase
        text = text.lower()

        # Replace spaces and special characters with the replacement character
        text = re.sub(r'[^a-z0-9]+', self.replacement_char, text)

        # Remove leading and trailing replacement characters
        text = text.strip(self.replacement_char)

        # Return the resulting slug
        return text
