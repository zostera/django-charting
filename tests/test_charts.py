from django.test import TestCase

from django_charting import Chart

TEST_TITLE = "test_titlé"


class TestChart(Chart):
    title = TEST_TITLE


class ChartTestCase(TestCase):
    def test_title(self):
        """Test setting and getting of title."""
        tc = TestChart()
        self.assertEqual(tc.title, TEST_TITLE)
        self.assertEqual(tc.title, tc.get_title())
