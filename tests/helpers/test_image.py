from unittest import TestCase

from image_examples.helpers.image import LazyImage


class TestLazyImage(TestCase):
    def test_implicit_comment(self):
        s = "ASDF"
        image = LazyImage(s)
        self.assertIn(s, image.comment)

    def test_explicit_comment(self):
        s = "ASDF"
        image = LazyImage("FOO", s)
        self.assertEqual(s, image.comment)

    def test_get_image(self):
        s = "usc_misc/4.2.03.tiff"
        image = LazyImage(s)
        self.assertIsNotNone(image)

    def test_get_image_filename(self):
        s = "usc_misc/4.2.03.tiff"
        image = LazyImage(s)
        self.assertIsNotNone(image.filename)
