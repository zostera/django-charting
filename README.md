# django-charting

[![CI](https://github.com/zostera/django-charting/workflows/CI/badge.svg?branch=main)](https://github.com/zostera/django-charting/actions?workflow=CI)
[![Coverage Status](https://coveralls.io/repos/github/zostera/django-icons/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-icons?branch=main)
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.python.org/pypi/django-icons)
[![Any color you like](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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
