import json
import datetime
from bson import ObjectId


def hexToObjectId(_hex):
    return ObjectId(_hex)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (ObjectId, datetime.date)):
            return str(o)

        return json.JSONEncoder.default(self, o)