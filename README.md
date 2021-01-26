# django-charting

Charts for Django using Google Charts API.

## Installation

Install `django-charting` using `pip`

```shell
pip install django-charting
```

## Quickstart

1. Add "django_charting" to your INSTALLED_APPS setting like this::

```python
INSTALLED_APPS = (
    # ...
    "django_charting",
    # ...
)
```

2. Create a basic chart like this:

```python
from django_charting import Chart, NumberColumn, StringColumn


class DemoChart(Chart):
    queryset = [
        {"project": "Project 1", "count": 75},
        {"project": "Project 2", "count": 25},
    ]
    type = "PieChart"
    title = "My demo"

    project = StringColumn()
    count = NumberColumn(accessor="count")
```


3. Render the chart in a template like this:

```
{% load django_charting %}

{% render_chart chart %}
```
