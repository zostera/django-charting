from django.test import TestCase

from django_charting import Chart, __version__

TEST_TITLE = "test_titlé"


class TestChart(Chart):
    title = TEST_TITLE


class VersionTestCase(TestCase):
    def test_version(self):
        """Test version."""
        self.assertEqual(__version__, "1.0.0")


class ChartTestCase(TestCase):
    def test_title(self):
        """Test setting and getting of title."""
        tc = TestChart()
        self.assertEqual(tc.title, TEST_TITLE)
        self.assertEqual(tc.title, tc.get_title())
