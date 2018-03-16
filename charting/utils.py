from __future__ import unicode_literals

import json
from django.utils.six import text_type


class ChartingJSONEncoder(json.JSONEncoder):
    """
    JSON encoder that handles date/time/datetime objects correctly.
    """
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return '__DATE__' + obj.isoformat() + '__DATE__'
        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            # This catches __proxy__object (lazy translations)
            return text_type(obj)


def get_javascript_object(value):
    return json.dumps(value, cls=ChartingJSONEncoder).replace('"__DATE__', 'new Date("').replace('__DATE__"', '")')
