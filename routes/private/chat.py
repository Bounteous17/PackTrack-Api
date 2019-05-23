from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from flask_restful import Resource, reqparse
from utils import functions as _functions, responses as _responses
from models import models as _models
from modules.user import user as _mUser
from modules.chat import chat as _mChat

parser = reqparse.RequestParser()


class Chat(Resource):
    # create new chat
    @jwt_required
    def post(self):
        try:
            parser.add_argument(
                'username', help='User with whom to start the chat', required=False)
            parser.add_argument('chat', help='Chat id', required=False)
            reqData = parser.parse_args()
            alloweds = []

            sUser = _mUser.findOne('username', reqData['username'])
            if _functions.resultError(sUser):
                return sUser.flaskResp()

            alloweds.append(sUser._id)
            creator = get_jwt_claims()
            alloweds.append(creator['identity'])

            newChat = _models.Chat(
                creator=creator['identity'],
                alloweds=alloweds
            )
            newChat.save()

            uUser = _mUser.findOneAndUpdate(
                '_id', creator['identity'], 'chats', newChat.id)
            if _functions.resultError(uUser):
                return uUser.flaskResp()

            uToUser = _mUser.findOneAndUpdate(
                '_id', sUser._id, 'chats', newChat.id)
            if _functions.resultError(uToUser):
                return uUser.flaskResp()

            return _functions.setModuleSuccess(payload='Chat initialized correctly', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error creating new chat, try it later ...', status=500).flaskResp()

    # list user chats
    @jwt_required
    def get(self):
        try:
            user = get_jwt_claims()
            sUser = _mUser.findOne('_id', user['identity'])
            if _functions.resultError(sUser):
                return sChat.flaskResp()
            userChats = _mUser.myChats(user['identity'])
            if _functions.resultError(sUser._id):
                return userChats.flaskResp()
            return _functions.setModuleSuccess(payload=list(userChats), key='mongo', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error listing chats, try it later ...', status=500).flaskResp()
