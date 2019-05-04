from utils import functions as _functions, validators as _validators, auth as _auth
from models import models as _models
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'Username is not optional', required = True)
parser.add_argument('password', help = 'Password is not optional', required = True)

class UserRegistration(Resource):
    def post(self):
        try:
            reqData = parser.parse_args()
            vPassword = _validators.checkPassword(reqData['password'])
            if _functions.resultError(vPassword):
                return vPassword.flaskResp()
            hashPassword = _auth.hashPassword(reqData['password'])
            if _functions.resultError(hashPassword):
                return hashPassword
            newRoundsMan = _models.User(
                username=reqData['username'],
                password=hashPassword,
            )
            newRoundsMan.save()
            return _functions.setModuleSuccess(payload='User created successfully', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error crating new user, try it later...', status=500).flaskResp()

