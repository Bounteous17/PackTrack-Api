import bcrypt
import jwt
from models import auth as _auth
from utils import functions as _functions
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

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

def createAccessToken(userId):
    return create_access_token(identity = userId)

def encodeJwt(user):
    try:
        return _auth.Tokens(
                    token=createAccessToken(str(user._id)),
                    rToken=create_refresh_token(identity = str(user._id))
                )
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error generating token, try it later...', status=500)
