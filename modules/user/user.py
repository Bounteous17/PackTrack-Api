from utils import functions as _functions, responses as _responses
from models import models as _models
from modules.db import utils as _mDbUtils
import bson

def myChats(userId):
    try:
        userChats = list(_models.User.objects.aggregate(*[
                    { '$match': { '_id': _mDbUtils.hexObjId(userId) } },
                    { '$unwind': '$chats' },
                    {
                        '$lookup':{
                            'from': _models.Chat._get_collection_name(),
                            'localField': 'chats',
                            'foreignField': '_id',
                            'as': 'chatObjects'
                        }
                    },
                    { '$unwind': '$chatObjects' },
                    { "$group": {
                        "_id": "$_id",
                        "chats": { "$push": "$chatObjects" }
                    }}
                ]))[0]
        return userChats['chats']
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error listing user chats ...', status=500)

def checkExists(field, value):
    try:
        return _models.User.objects.get(** {'{}'.format(field): value})
    except _models.User.DoesNotExist:
       return False
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error check user exists ...', status=500)

def findById(userId):
    try:
        return _models.User.objects.get(_id = userId)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find user ...', status=500)

def findOne(field, value):
    try:
        condition = {'{}'.format(field): value}
        checkUser = checkExists(field, value)
        if _functions.resultError(checkUser):
            return checkUser
        if not checkUser:
            return _responses.userNotFound()
        return _models.User.objects.get(** condition)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find user ...', status=500)

def findOneAndUpdate(field, value, uField, uValue):
    try:
        condition = {'{}'.format(field): value}
        checkUser = checkExists(field, value)
        if _functions.resultError(checkUser):
            return checkUser
        if not checkUser:
            return _responses.userNotFound()
        return _models.User.objects(** condition).update_one(push__chats=uValue)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error updating user ...', status=500)


def selectInfo(fields, User):
    info = {}
    for field in fields:
        if User[field]:
            info[field] = User[field]
    return info
