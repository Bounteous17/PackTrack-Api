from utils import functions as _functions, validators as _validators, auth as _auth
from models import roundsman as _roundsman


def login(reqData):
    try:
        valid = _validators.checkMinData(reqData, ['email', 'password'])
        if _functions.resultError(valid):
            return valid

        user = _roundsman.RoundsMan.objects.get(email = reqData['email'])
        if user is None:
            return _functions.setModuleError(payload='Email not found on DB', error='User not found, try it later...', status=404)
        unHashPassword = _auth.unHashPassword(reqData['password'], user['password'])
        if _functions.resultError(unHashPassword):
            return unHashPassword
    
        return _functions.setModuleSuccess(payload='User login success', status=200)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error login user, try it later...')
