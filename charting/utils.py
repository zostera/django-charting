from __future__ import unicode_literals

import json
import datetime


class ChartingJSONEncoder(json.JSONEncoder):
    """
    JSON encoder that handles date/time/datetime objects correctly.
    """

    def __init__(self):
        json.JSONEncoder.__init__(self, separators=(",", ":"), ensure_ascii=False)

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return super(ChartingJSONEncoder, self).default(obj)


def json_encode(value):
    return json.dumps(value, cls=ChartingJSONEncoder)