from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from flask_restful import Resource, reqparse, request
from utils import functions as _functions, responses as _responses
from models import models as _models
from modules.user import user as _mUser
from modules.chat import chat as _mChat, shared as _mSharedChat
from modules.message import shared as _mSharedMessage

parser = reqparse.RequestParser()


class Message(Resource):
    # newchat message
    @jwt_required
    def post(self):
        try:
            args = request.args
            parser.add_argument('message', help='Chat message', required=True)
            reqData = parser.parse_args()
            userId = get_jwt_claims()
            userAllowed = _mSharedChat.allowedRead(userId['identity'])
            if _functions.resultError(userAllowed):
                return userAllowed.flaskResp()
            sChat = _mChat.findById(args['chatId'])
            if _functions.resultError(sChat):
                return sChat.flaskResp()
            new_message = {
                'message': reqData['message'],
                'from': userId['identity'],
                'read': False,
            }
            uChat = _mSharedMessage.new(sChat.id, new_message)
            if _functions.resultError(uChat):
                return uChat.flaskResp()
            return _functions.setModuleSuccess(payload=uChat.messages, key='mongo', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error posting new message', status=500).flaskResp()

    # list messages
    @jwt_required
    def get(self):
        try:
            args = request.args
            userId = get_jwt_claims()
            userAllowed = _mSharedChat.allowedRead(userId['identity'])
            if _functions.resultError(userAllowed):
                return userAllowed.flaskResp()
            sChat = _mChat.findById(args['chatId'])
            if _functions.resultError(sChat):
                return sChat.flaskResp()
            return _functions.setModuleSuccess(payload=sChat.messages, key='mongo', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error posting new message', status=500).flaskResp()
