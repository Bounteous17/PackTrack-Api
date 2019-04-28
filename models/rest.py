from flask import make_response as FlaskResponse, jsonify
from json import JSONEncoder

class ModuleStatus():
    def __init__(self, **args):
        self.status = args.get('status')
        self.payload = args.get('payload')
        self.error = args.get('error')
        self.key = args.get('key')

    def setStatus(self):
        if self.status is None or 200 < self.status > 501:
            self.status = 500

    def flaskResp(self):
        send = self.payload
        if self.error is not None:
            send = self.error
        if self.key is None:
            self.key = 'message'
        if self.key is not 'master':
            return { self.key: send }, self.status
        return send, self.status

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
