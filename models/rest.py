from flask import make_response as FlaskResponse, jsonify
import json

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
            self.key = 'msg'
        elif self.key == 'master':
            return send, self.status
        elif self.key == 'encode':
            return jsonify(send), self.status
        elif self.key == 'list':
            return json.dumps(send, default=str), self.status
        return { self.key: send }, self.status
