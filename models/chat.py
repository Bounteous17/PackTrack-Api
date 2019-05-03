from mongoengine import *
import datetime
from models import user as _modelUser

class Chat(Document):
    _id = ObjectIdField()
    creator = ReferenceField(_modelUser.User)
    messages = ListField(default=[])
    alloweds = ListField(ReferenceField(_modelUser.User), default=[])
    created = DateTimeField(default=datetime.datetime.now)
