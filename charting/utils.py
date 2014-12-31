from __future__ import unicode_literals

import json
import datetime


class ChartingJSONEncoder(json.JSONEncoder):
    """
    JSON encoder that handles date/time/datetime objects correctly.
    """
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return '__DATE__' + obj.isoformat() + '__DATE__'
        return json.JSONEncoder.default(self, obj)


def json_encode(value):
    return json.dumps(value, cls=ChartingJSONEncoder).replace('"__DATE__', 'new Date("').replace('__DATE__"', '")')