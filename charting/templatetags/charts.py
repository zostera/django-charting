from __future__ import unicode_literals

from django import template


register = template.Library()


@register.inclusion_tag('charts/chart.html')
def render_chart(chart):
    return {
        'chart': chart,
    }
