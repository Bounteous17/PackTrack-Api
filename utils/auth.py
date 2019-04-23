import bcrypt
from utils import functions as _functions

def hashPassword(p_password):
    try:
        e_p_password = p_password.encode()
        sal = bcrypt.gensalt()
        return bcrypt.hashpw(e_p_password, sal)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error hashing password, try it later...', status=500)

def unHashPassword(p_password, h_password):
    try:
        if not bcrypt.checkpw(p_password.encode(), h_password.encode()):
            return _functions.setModuleError(payload=e, error='Bad password', status=401)
        return True
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error unhashing password, try it later...', status=500)
