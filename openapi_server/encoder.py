from flask.json.provider import JSONProvider
import datetime

class JSONEncoder(JSONProvider):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        return super().default(o)
