from django.test import TestCase


class VersionTestCase(TestCase):
    """Test presence of package version."""

    def test_version(self):
        import django_charting

        version = django_charting.__version__
        version_parts = version.split(".")
        self.assertTrue(len(version_parts) >= 2)
