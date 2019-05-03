from mongoengine import *
import datetime

class User(Document):
    _id = ObjectIdField()
    username = StringField(required=True, min_length=2, max_length=50, unique=True)
    password = StringField(required=True)
    created = DateTimeField(default=datetime.datetime.now)
