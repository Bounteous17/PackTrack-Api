from utils import functions as _functions

def userNotFound():
    return _functions.setModuleError(payload='User not found', error='User not found ...', status=404)
