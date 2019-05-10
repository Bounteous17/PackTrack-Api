from utils import functions as _functions, db as _utilsDb
from models import models as _models

def allowedRead(userId):
    try:
        userAllowed = _models.Chat.objects(alloweds__contains=_utilsDb.hexToObjectId(userId))
        if userAllowed:
            return True
        return _functions.setModuleError(payload='userId is not in alloweds array', error='User not allowed to access the chat')
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error checking if user is allowed to access chat ...', status=500)
