from utils import functions as _functions

def chatNotFound():
    return _functions.setModuleError(payload='Chat not found', error='Chat not found ...', status=404)

def userNotFound():
    return _functions.setModuleError(payload='User not found', error='User not found ...', status=404)

def unwantedRes(objName):
    if objName is 'user':
        return ['_id', 'created', 'password', 'chats']