import bcrypt
from utils import functions as _functions

def hashPassword(p_password):
    try:
        e_p_password = p_password.encode()
        sal = bcrypt.gensalt()
        return bcrypt.hashpw(e_p_password, sal)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error hashing password, try it later...', status=500)
