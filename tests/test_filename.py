from unittest import TestCase

from image_examples import peppers, phantom


class TestFilename(TestCase):
    def test_one_image_by_name(self):
        value = peppers.filename
        self.assertIsNotNone(value)
        
    def test_another_image_by_name(self):
        value = phantom.filename
        self.assertIsNotNone(value)
        
