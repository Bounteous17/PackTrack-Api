from flask import make_response as FlaskResponse, jsonify

class ModuleStatus():
    def __init__(self, **args):
        self.status = args.get('status')
        self.payload = args.get('payload')
        self.error = args.get('error')

    def setStatus(self):
        if self.status is None or 200 < self.status > 501:
            self.status = 500

    def flaskResp(self):
        return FlaskResponse(jsonify(self.send), self.status)