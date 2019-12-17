from unittest import TestCase

from image_examples import aliases, peppers, phantom


class TestAliases(TestCase):
    def test_one_image_by_name(self):
        value = peppers.filename
        self.assertIsNotNone(value)
        
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

