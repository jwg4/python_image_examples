from unittest import TestCase

from image_examples import filenames


class TestFilename(TestCase):
    def test_one_image_by_name(self):
        value = filenames.peppers
        self.assertIsNotNone(value)
        
    def test_another_image_by_name(self):
        value = filenames.phantom
        self.assertIsNotNone(value)
        
