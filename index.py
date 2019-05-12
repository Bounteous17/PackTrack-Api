#!flask/bin/python
# Module imports
from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

from utils import functions as _functions, auth as _auth
# Routes imports
from routes.public import status as _status, signup as _signup, login as _login
from routes.private import user as _privUser, auth as _privAuth, chat as _privChat, message as _privMessage
# Models
from models import rest as _rest, redis as _redis, auth as _modelAuth
# Modules
from modules.db import db as _db, tmp_db as _tmpDb

_db.instance()

app = Flask(__name__) # Create http server
CORS(app)

_Config = _functions.Config
if _functions.resultError(_Config):
    exit(1)

app.secret_key = _Config['app']['secret']

api = Api(app)
socketio = SocketIO(app)

ACCESS_EXPIRES = _tmpDb.TokensExpires.access_expires
REFRESH_EXPIRES = _tmpDb.TokensExpires.refresh_expires

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_EXPIRES
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_SECRET_KEY'] = _Config['jwt']['secret']
app.config['JWT_ALGORITHM'] = _Config['jwt']['algorithm']
jwt = JWTManager(app)

# app.config['DEBUG'] = _Config['dev']['debug']

users = {}

@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    entry = _tmpDb.RevokeInstance.get(jti)
    if entry is None:
        return True
    return entry == 'true'

@app.route('/orginate')
def orginate():
    socketio.emit('server orginated', 'Something happened on the server!')
    return '<h1>Sent!</h1>'

@socketio.on('message from user', namespace='/messages')
def receive_message_from_user(message):
    print('USER MESSAGE: {}'.format(message))
    emit('from flask', message.upper(), broadcast=True)

@socketio.on('username', namespace='/private')
def receive_username(username):
    users[username] = request.sid
    #users.append({username : request.sid})
    #print(users)
    print(f'Username {username} added!')

@socketio.on('private_message', namespace='/private')
def private_message(payload):
    username = payload['username']
    recipient_session_id = users[username]
    message = payload['message']
    print (f'Message {message} sent to {username} with id {recipient_session_id}')
    emit('new_private_message', message, room=recipient_session_id)

# Append routes
api.add_resource(_signup.UserRegistration, '/signup')
api.add_resource(_login.UserLogin, '/login')
# Private
api.add_resource(_privUser.Info, '/user')
api.add_resource(_privAuth.Auth, '/auth')
api.add_resource(_privChat.Chat, '/chat')
api.add_resource(_privMessage.Message, '/message')

#Start APP multiple CPUs
app.run(host='0.0.0.0', threaded=_Config['app']['threaded'])
