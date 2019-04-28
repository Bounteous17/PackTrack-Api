from utils import functions as _functions
from models import user as _user
import bson

def findById(userId):
    try:
        return _user.User.objects.get(_id = userId)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find user ...', status=500)

def findOne(field, value):
    try:
        return _user.User.objects.get(**{'{}'.format(field): value})
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find user ...', status=500)

def selectInfo(fields, User):
    info = {}
    for field in fields:
        if User[field]:
            info[field] = User[field]
    return info
