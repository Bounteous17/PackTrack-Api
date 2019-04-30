from utils import functions as _functions, validators as _validators, auth as _auth
from models import user as _user
from modules.db import tmp_db as _tmpDb
from modules.user import user as _moduleUser
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
)

parser = reqparse.RequestParser()
parser.add_argument('email', help = "Email can not be blank", required = True)
parser.add_argument('password', help = "Password can not be blank", required = True)

class UserLogin(Resource):
    def post(self):
        try:
            reqData = parser.parse_args()
            user = _moduleUser.findOne('email', reqData['email'])
            if user is None:
                return _functions.setModuleError(payload='Email not found on DB', error='User not found, try it later...', status=404).flaskResp()
            unHashPassword = _auth.unHashPassword(reqData['password'], user['password'])
            if _functions.resultError(unHashPassword):
                return unHashPasswordv.flaskResp()
            tokens = _auth.encodeJwt(user)
            if _functions.resultError(tokens):
                return token.flaskResp()
            access_jti = get_jti(encoded_token=tokens.token)
            refresh_jti = get_jti(encoded_token=tokens.rToken)

            _tmpDb.RevokeInstance.set(access_jti, 'false', _tmpDb.TokensExpires.access_expires * 1.2)
            _tmpDb.RevokeInstance.set(refresh_jti, 'false', _tmpDb.TokensExpires.refresh_expires * 1.2)

            return _functions.setModuleSuccess(payload={'access_token': tokens.token, 'refresh_token':  tokens.rToken}, key='tokens', status=201).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error login user, try it later...', status=500).flaskResp()
