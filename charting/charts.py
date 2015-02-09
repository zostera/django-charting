from __future__ import unicode_literals

import uuid

from .utils import get_javascript_object
from .columns import BaseColumn


class Chart(object):
    id = None
    title = None
    data = None
    queryset = None

    # Private
    _id = None

    def __init__(self, queryset=None):
        super(Chart, self).__init__()
        if queryset is not None:
            self.queryset = queryset


    def get_element_id(self):
        if not self._id:
            if self.id:
                self._id = self.id
            else:
                self._id = 'django-chart-{uuid}'.format(uuid=uuid.uuid4())
        return self._id

    def get_title(self):
        return self.title

    def get_type(self):
        return self.type

    def get_options(self):
        options = {}
        title = self.get_title()
        if title:
            options['title'] = title
        return options

    def get_queryset(self):
        return self.queryset

    def get_data(self):
        if self.data:
            return self.data
        return self.get_queryset()

    def get_data_table(self):
        # Start with empty rows and columns
        cols = []
        rows = []
        # Lookup for columns
        columns = []
        # Walk the attributes in reversed order
        for name in dir(self):
            # We only need BaseColumns
            column = getattr(self, name)
            if not isinstance(column, BaseColumn):
                continue
            # Set the accessor if it's not known
            if not column.accessor:
                column.accessor = name
            columns.append({
                'name': name,
                'sort_order': column._sort_order,
                'column': column,
                'data': column.get_data_table_column(name),
            })
        # Sort columns
        columns = sorted(columns, key=lambda x: x['sort_order'])
        for column in columns:
            cols.append(column['data'])
        for item in self.get_data():
            cells = []
            for column in columns:
                cell = column['column'].get_data_table_cell(item)
                try:
                    render = getattr(self, 'render_{name}'.format(name=column['name']))
                except AttributeError:
                    pass
                else:
                    cell = render(cell=cell, item=item)
                cells.append(cell)
            rows.append({'c': cells})
        return {
            'cols': cols,
            'rows': rows,
            'p': {},
        }

    def get_chart_wrapper_data_as_json(self):
        wrapper = {
            'chartType': self.get_type(),
            'dataTable': self.get_data_table(),
            'options': self.get_options(),
            'containerId': self.get_element_id(),
        }
        return get_javascript_object(wrapper)
