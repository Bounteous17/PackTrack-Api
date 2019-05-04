from utils import functions as _functions, responses as _responses
from models import models as _models
import bson

def checkExists(field, value):
    try:
        print (field, value)
        return _models.Chat.objects.get(** {'{}'.format(field): value})
    except _models.Chat.DoesNotExist:
        return False
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error check chat exists ...', status=500)

def findById(chatId):
    try:
        return _models.Chat.objects.get(_id = chatId)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find chat ...', status=500)

def findOne(field, value):
    try:
        condition = {'{}'.format(field): value}
        checkChat = checkExists(field, value)
        if _functions.resultError(checkChat):
            return checkChat
        if not checkChat:
            return _responses.chatNotFound()
        return _models.Chat.objects.get(** condition)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error find chat ...', status=500)

def findOneAndUpdate(field, value, uField, uValue):
    try:
        condition = {'{}'.format(field): value}
        checkChat = checkExists(field, value)
        if _functions.resultError(checkChat):
            return checkChat
        if not checkChat:
            return _responses.userNotFound()
        return _models.Chat.objects(** condition).update_one(push__chats=uValue)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error updating chat ...', status=500)


def selectInfo(fields, User):
    info = {}
    for field in fields:
        if Chat[field]:
            info[field] = Chat[field]
    return info
