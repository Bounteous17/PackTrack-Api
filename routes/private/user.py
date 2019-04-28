from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from modules.user import user as _mUser
from models import rest as _rest
from utils import functions as _functions
parser = reqparse.RequestParser()

class Info(Resource):
    @jwt_required
    def get(self):
        try:
            userId = get_jwt_identity()
            sUser = _mUser.findById(userId)
            if sUser is None:
                return _functions.setModuleError(payload='User not found for jwt provided', error='User not found ...', status=404).flaskResp()
            if _functions.resultError(sUser):
                return sUser.flaskResp()
            return _functions.setModuleSuccess(payload=_mUser.selectInfo(['email', 'dni', 'name', 'surname', 'age'], sUser), key='master', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error accessing user information ...').flaskResp()
