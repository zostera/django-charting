from django.template import Context, Template
from django.test import TestCase

from django_charting import Chart, NumberColumn, StringColumn


class TestChart(Chart):
    queryset = [
        {
            "project": "Project 1",
            "count": 75,
        },
        {
            "project": "Project 2",
            "count": 25,
        },
    ]
    type = "PieChart"
    title = "My demo"

    project = StringColumn()
    count = NumberColumn(accessor="count")


def render_template(content, **context_args):
    """Create a template with content ``content`` that first loads the ``django_charting`` library."""
    template = Template("{% load django_charting %}" + content)
    return template.render(Context(context_args))


class TemplateTagsTest(TestCase):
    """Test all template tags."""

    def test_load_template_tags(self):
        """Assert that template tags can be loaded."""
        self.assertEqual(render_template(""), "")

    def test_render_chart_none(self):
        """Render a chart that is None."""
        self.assertEqual(render_template("{% render_chart chart %}", chart=None), "")

    def test_render_chart(self):
        """Render a chart."""
        html = render_template("{% render_chart chart %}", chart=TestChart())
        self.assertIn("javascript", html)
        self.assertIn("google.com", html)
