import bcrypt
import jwt
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
            return _functions.setModuleError(payload='Hases not equals', error='Bad password', status=401)
        return True
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error unhashing password, try it later...', status=500)

def encodeJwt(user):
    try:
        print (str(user['_id']))
        token = jwt.encode({
                '_id': str(user['_id']),
                'dni': user['dni']
            }, _functions.Config['jwt']['secret'], _functions.Config['jwt']['algorithm'])
        return token
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error generating token, try it later...', status=500)
