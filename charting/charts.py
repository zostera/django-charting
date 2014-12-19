from __future__ import unicode_literals
from collections import OrderedDict

import json
import uuid

from .columns import BaseColumn


class Chart(object):
    id = None
    title = None
    data = None
    queryset = None

    # Private
    _id = None

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
        columns = OrderedDict({})
        # Get all attributes
        attrs = dir(self)
        # Walk the attributes in reversed order
        for name in attrs[::-1]:
            # We only need BaseColumns
            column = self.__getattribute__(name)
            if not isinstance(column, BaseColumn):
                continue
            # Set the accessor if it's not known
            if not column.accessor:
                column.accessor = name
            cols.append(column.get_data_table_column(name))
            columns[name] = column
        for item in self.get_data():
            cells = []
            for name in columns:
                cell = columns[name].get_data_table_cell(item)
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
        return json.dumps(wrapper)
