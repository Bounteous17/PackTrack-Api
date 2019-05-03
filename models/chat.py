from mongoengine import *
import datetime

class Chat(Document):
    _id = ObjectIdField()
    messages = ListField(default=[])
    created = DateTimeField(default=datetime.datetime.now)
