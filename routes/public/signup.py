from utils import functions as _functions, validators as _validators, auth as _auth
from models import roundsman as _roundsman


def signup(reqData):
    try:
        valid = _validators.checkMinData(reqData, ['dni', 'name', 'surname', 'age', 'city', 'street', 'post_code', 'email', 'password'])
        if _functions.resultError(valid):
            return valid
        hashPassword = _auth.hashPassword(reqData['password'])
        if _functions.resultError(hashPassword):
            return hashPassword
        newRoundsMan = _roundsman.RoundsMan(
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
        return _functions.setModuleSuccess(payload='User created successfully', status=200)
    except Exception as e:
        return _functions.setModuleError(payload=e, error='Error crating new user, try it later...')
