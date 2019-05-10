from utils import functions as _functions, db as _utilsDb
from models import models as _models

def new(chatId, new_message):
    try:
        new_message['from'] = _utilsDb.hexToObjectId(new_message['from'])
        _models.Chat.objects(id=chatId).update_one(push__messages=new_message)
        return _models.Chat.objects.get(id = chatId)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error list chat messages ...', status=500)
