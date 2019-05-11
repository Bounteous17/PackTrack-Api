from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from utils import functions as _functions, responses as _responses
from models import models as _models
from modules.user import user as _mUser
from modules.chat import chat as _mChat, shared as _mSharedChat
from modules.message import shared as _mSharedMessage

parser = reqparse.RequestParser()
parser.add_argument('message', help = 'Chat message', required = True)

class Message(Resource):
    #newchat message
    @jwt_required
    def post(self):
        try:
            parser.add_argument('chat', help = 'Chat id', required = True)
            reqData = parser.parse_args()
            userId = get_jwt_identity()
            userAllowed = _mSharedChat.allowedRead(userId)
            if _functions.resultError(userAllowed):
                return userAllowed.flaskResp()
            sChat = _mChat.findById(reqData['chat'])
            if _functions.resultError(sChat):
                return sChat.flaskResp()
            new_message = {
                        'message': reqData['message'],
                        'from': userId,
                        'read': False,
                    }
            uChat = _mSharedMessage.new(sChat.id, new_message)
            if _functions.resultError(uChat):
                return uChat.flaskResp()
            return _functions.setModuleSuccess(payload=uChat.messages, key='list', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error posting new message', status=500).flaskResp()
