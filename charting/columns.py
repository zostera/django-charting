from __future__ import unicode_literals

from django.utils.text import slugify
from django.utils.six import text_type


class BaseColumn(object):
    _sort_by_creation = 0
    type = None
    accessor = None
    label = None

    def __init__(self, *args, **kwargs):
        super(BaseColumn, self).__init__()
        self._sort_order = BaseColumn._sort_by_creation
        self.accessor = kwargs.get('accessor', None)
        self.label = kwargs.get('label', None)
        BaseColumn._sort_by_creation += 1

    def get_id(self, name):
        return slugify(name)

    def get_label(self, name):
        if self.label:
            return text_type(self.label)
        return name

    def get_type(self):
        return text_type(self.type)

    def get_data_table_column(self, name):
        unicode_name = text_type(name)
        return {
            'id': self.get_id(unicode_name),
            'label': self.get_label(unicode_name),
            'type': self.get_type(),
        }

    def get_value(self, value):
        return value

    def get_string(self, value):
        return None

    def get_data_table_cell(self, item):
        # No item, no cell
        if item is None:
            return None
        # Get value from object or dict
        try:
            value = getattr(item, self.accessor)
        except AttributeError:
            try:
                value = item.get(self.accessor)
            except AttributeError:
                value = None
        # Get various presentations
        value = self.get_value(value)
        cell = {'v': value}
        string = self.get_string(value)
        if string is not None:
            cell['f'] = string
        return cell


class StringColumn(BaseColumn):
    type = 'string'

    def get_value(self, value):
        return text_type(value)


class NumberColumn(BaseColumn):
    type = 'number'

    def get_value(self, value):
        return float(value)


class DateColumn(BaseColumn):
    type = 'date'
