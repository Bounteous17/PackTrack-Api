from utils import functions as _functions, validators as _validators, auth as _auth
from models import user as _user
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('dni', help = 'Dni is not optional', required = True)
parser.add_argument('name', help = 'Name is not optional', required = True)
parser.add_argument('email', help = 'Dni is not optional', required = True)
parser.add_argument('password', help = 'Dni is not optional', required = True)
parser.add_argument('surname', help = 'User surname', required = False)
parser.add_argument('age', help = 'User ages', required = False)
parser.add_argument('city', help = 'User city', required = False)
parser.add_argument('street', help = 'User street', required = False)
parser.add_argument('post_code', help = 'User ZIP', required = False)

class UserRegistration(Resource):
    def post(self):
        try:
            reqData = parser.parse_args()
            hashPassword = _auth.hashPassword(reqData['password'])
            if _functions.resultError(hashPassword):
                return hashPassword
            newRoundsMan = _user.User(
                email=reqData['email'],
                password=hashPassword,
                dni=reqData['dni'],
                name=reqData['name'],
                surname=reqData['surname'],
                age=reqData['age'],
                city=reqData['city'],
                street=reqData['street'],
                post_code=reqData['post_code']
            )
            newRoundsMan.save()
            return _functions.setModuleSuccess(payload='User created successfully', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error crating new user, try it later...', status=500).flaskResp()

