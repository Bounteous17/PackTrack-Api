from mongoengine import *
import datetime

class RoundsMan(Document):
    _id = ObjectIdField()
    email = StringField(required=True, max_length=50, unique=True)
    password = StringField(required=True)
    dni = StringField(required=True, length=9, unique=True)
    name = StringField(required=True, max_length=50)
    surname = StringField(required=True, max_length=50)
    age = IntField(required=True, min_value=18, max_value=99)
    city = StringField(required=True, max_length=50)
    street = StringField(required=True, max_length=50)
    post_code = IntField(required=True, min_value=0, max_value=99999)
    date = DateTimeField(default=datetime.datetime.now)
