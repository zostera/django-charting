from django_charting import Chart, NumberColumn, StringColumn


class DemoChart(Chart):
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
