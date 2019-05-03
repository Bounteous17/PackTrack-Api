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
        condition = {'{}'.format(field): value}
        if _user.User.objects.filter(** condition).count() > 0:
            return _user.User.objects.get(** condition)
        return _functions.setModuleError(payload='User not found on users collection', error='User not found ...', status=404)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find user ...', status=500)

def selectInfo(fields, User):
    info = {}
    for field in fields:
        if User[field]:
            info[field] = User[field]
    return info
