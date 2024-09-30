import re

def slugify(text):
    # Convert the text to lowercase
    text = text.lower()

    # Replace spaces and special characters with hyphens using regex
    text = re.sub(r'[^a-z0-9]+', '-', text)

    # Remove leading and trailing hyphens
    text = text.strip('-')

    # Return the resulting slug
    return text
