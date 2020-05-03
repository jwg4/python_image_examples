import os

from unittest import TestCase

from image_examples import cameraman


class TestCameramanImage(TestCase):
    def test_filename_exists(self):
        value = cameraman.filename
        self.assertIsNotNone(value)

    def test_file_exists(self):
        value = cameraman.filename
        exists = os.path.isfile(value)
        self.assertTrue(exists, "%s does not exist" % (value, ))
    
    def test_data_can_be_loaded(self):
        data = cameraman.data
        self.assertIsNotNone(data)
    
    def test_can_retrieve_alias(self):
        self.assertEqual(cameraman.alias, "cameraman")
