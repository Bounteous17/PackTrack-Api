from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from utils import functions as _functions, responses as _responses
from models import chat as _modelChat
from modules.user import user as _mUser

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'User with whom to start the chat', required = True)

class Chat(Resource):
    #create new chat
    @jwt_required
    def post(self):
        try:
            reqData = parser.parse_args()
            alloweds = []
            sUser = _mUser.findOne('username', reqData['username'])
            if _functions.resultError(sUser):
                return sUser.flaskResp()
            if sUser is None:
                return _responses.userNotFound().flaskResp()
            print (sUser)
            alloweds.append(sUser._id)
            creator = get_jwt_identity()
            alloweds.append(creator)
            newChat = _modelChat.Chat(
                    creator=creator,
                    alloweds=alloweds
            )
            newChat.save()
            return _functions.setModuleSuccess(payload='Chat initialized correctly', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error creating new chat, try it later ...', status=500).flaskResp()
