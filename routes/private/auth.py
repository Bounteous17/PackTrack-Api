from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_raw_jwt, get_jti
from utils import functions as _functions, auth as _utilAuth
from modules.db import tmp_db as _tmpDb

ACCESS_EXPIRES = _tmpDb.TokensExpires.access_expires
REFRESH_EXPIRES = _tmpDb.TokensExpires.refresh_expires

class Auth(Resource):
    @jwt_required
    # Refresh token
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = _utilAuth.createAccessToken(current_user)
            access_jti = get_jti(encoded_token=access_token)
            _tmpDb.RevokeInstance.set(access_jti, 'false', ACCESS_EXPIRES * 1.2)
            return _functions.setModuleSuccess(payload={'access_token': access_token}, key='master', status=201).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error refreshing token ...').flaskResp()

    @jwt_required
    # Remove token (logout)
    def delete(self):
        try:
            jti = get_raw_jwt()['jti']
            _tmpDb.RevokeInstance.set(jti, 'true', ACCESS_EXPIRES * 1.2)
            return _functions.setModuleSuccess(payload='Access token revoked', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error access token revoked ...', status=500).flaskResp()
