from __future__ import unicode_literals

from charting import Chart, StringColumn, NumberColumn


class DemoChart(Chart):
    queryset = [
        {'project': 'Project 1', 'count': 75, },
        {'project': 'Project 2', 'count': 25, },
    ]
    type = 'PieChart'
    title = 'My demo'

    project = StringColumn()
    count = NumberColumn(accessor='count')