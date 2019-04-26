from utils import functions as _functions, validators as _validators, auth as _auth
from models import roundsman as _roundsman
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('email', help = "Email can not be blank", required = True)
parser.add_argument('password', help = "Password can not be blank", required = True)

class UserLogin(Resource):
    def post(self):
        try:
            reqData = parser.parse_args()
            user = _roundsman.RoundsMan.objects.get(email = reqData['email'])
            if user is None:
                return _functions.setModuleError(payload='Email not found on DB', error='User not found, try it later...', status=404).flaskResp()
            unHashPassword = _auth.unHashPassword(reqData['password'], user['password'])
            if _functions.resultError(unHashPassword):
                return unHashPasswordv.flaskResp()
            token = _auth.encodeJwt(user)
            if _functions.resultError(token):
                return token.flaskResp()
    
            res = _functions.setModuleSuccess(payload=token, key='token', status=200).flaskResp()
            return res
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error login user, try it later...', status=500).flaskResp()
