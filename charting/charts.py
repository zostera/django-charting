from __future__ import unicode_literals
import json


class Chart(object):
    queryset = None
    title = None
    type = None
    columns = [
        {'label': 'Object', 'type': 'string'},
        {'label': 'One', 'type': 'number'},
    ]

    def __init__(self, queryset=None, title=None):
        if queryset is not None:
            self.queryset = queryset
        if title is not None:
            self.title = title

    def get_title(self):
        return self.title

    def get_queryset(self):
        return self.queryset

    def get_columns(self):
        return self.columns

    def get_row(self, item):
        return {
            'c': [
                {'v': unicode(item)},
                {'v': 1, 'f': '1', },
            ]
        }

    def get_rows(self):
        rows = []
        for item in self.get_queryset().all():
            rows.append(self.get_row(item))
        return rows

    def get_data(self):
        data = {
            'cols': self.get_columns(),
            'rows': self.get_rows(),
        }
        return json.dumps(data)

    def get_type(self):
        return self.type

    def get_width(self):
        return 400

    def get_height(self):
        return 300

    def get_options(self):
        options = {
            'title': self.get_title(),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return json.dumps(options)
