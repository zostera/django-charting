from django.test import TestCase


class BaseTest(TestCase):
    """Test the Font Awesome Renderer."""

    def test_version(self):
        from django_charting import __version__

        parts = __version__.split(".")
        self.assertEqual(len(parts), 3)
