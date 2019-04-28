from datetime import timedelta

class Redis():
    def  __init__(self, **args):
        self.host = args.get('host')
        self.port = args.get('port')
        self.db = args.get('db')

class Expires():
    def __init__(self, **args):
        self.access_expires = timedelta(args.get('access_expires'))
        self.refresh_expires = timedelta(args.get('refresh_expires'))
