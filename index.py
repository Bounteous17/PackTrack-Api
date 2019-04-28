#!flask/bin/python
# Module imports
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from utils import functions as _functions
# Routes imports
from routes.public import status as _status, signup as _signup, login as _login
from routes.private import user as _privUser
# Models
from models import rest as _rest, redis as _redis
# Modules
from modules.db import db as _db, tmp_db as _tmpDb

_db.instance()

app = Flask(__name__) # Create http server

_Config = _functions.Config
if _functions.resultError(_Config):
    exit(1)

api = Api(app)

app.secret_key = _Config['app']['secret']

ACCESS_EXPIRES = _tmpDb.TokensExpires.access_expires
REFRESH_EXPIRES = _tmpDb.TokensExpires.refresh_expires

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_EXPIRES
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_SECRET_KEY'] = _Config['jwt']['secret']
jwt = JWTManager(app)

app.config['DEBUG'] = _Config['dev']['debug']

@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    entry = _tmpDb.RevokeInstance.get(jti)
    if entry is None:
        return True
    return entry == 'true'

# Append routes
api.add_resource(_signup.UserRegistration, '/signup')
api.add_resource(_login.UserLogin, '/login')
# Private
api.add_resource(_privUser.Info, '/user')

app.run()
