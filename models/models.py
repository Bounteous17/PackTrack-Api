import datetime
from mongoengine import *
from bson import json_util

class User(Document):
    _id = ObjectIdField()
    username = StringField(required=True, min_length=2, max_length=50, unique=True)
    password = StringField(required=True)
    chats = ListField(ReferenceField('Chat'), defaults=[])
    created = DateTimeField(default=datetime.datetime.now)

    def to_json(self):
            return self.to_mongo()
            #return json_util.dumps(data)

class Chat(Document):
    creator = ReferenceField('User')
    messages = ListField(default=[])
    alloweds = ListField(ReferenceField('User'), default=[])
    created = DateTimeField(default=datetime.datetime.now)
    valid = BooleanField(default=False)
