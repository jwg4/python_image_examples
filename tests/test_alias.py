import os

from unittest import TestCase

from image_examples import aliases, peppers, phantom


class TestAliases(TestCase):
    def test_one_image_by_name(self):
        value = peppers.filename
        self.assertIsNotNone(value)

    def test_file_exists(self):
        value = peppers.filename
        exists = os.path.isfile(value)
        self.assertTrue(exists, "%s does not exist" % (value, ))

    def test_another_image_by_name(self):
        value = phantom.filename
        self.assertIsNotNone(value)


class TestAliasesObject(TestCase):
    def test_one_image_by_name(self):
        value = aliases.peppers.filename
        self.assertIsNotNone(value)
        
    def test_another_image_by_name(self):
        value = aliases.phantom.filename
        self.assertIsNotNone(value)

    def test_other_main_images_by_name(self):
        names = [
            "fishing_boat",
            "mandrill",
            "cameraman"
          ]
        for name in names:
            value = getattr(aliases, name)
            self.assertIsNotNone(value, "Alias %s does not exist" % (name,))


class TestAliasMetadata(TestCase):
    def test_metadata_dict(self):
        data = aliases.metadata
        self.assertIn("fishing_boat", data)
