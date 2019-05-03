from utils import functions as _functions
from models import chat as _modelChat
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'User with whom to start the chat', required = True)

class Chat(Resource):
    #create new chat
    def post(self):
        try:
            reqData = parser.parse_args()
            newChat = _modelChat.Chat()
            newChat.save()
            return _functions.setModuleSuccess(payload='Chat initialized correctly', status=200).flaskResp()
        except Exception as e:
            return _functions.setModuleError(payload=e, error='Error creating new chat, try it later ...', status=500).flaskResp()
