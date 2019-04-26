#!flask/bin/python
# Module imports
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from utils import functions as _functions
# Routes imports
from routes.public import status as _status, signup as _signup, login as _login
# Models
from models import rest as _rest
# Modules
from modules.db import db as _db

_db.instance()

app = Flask(__name__) # Create http server
api = Api(app)

_Config = _functions.Config
if _functions.resultError(_Config):
    exit(1)

app.config['DEBUG'] = _Config['dev']['debug']
app.config['JWT_SECRET_KEY'] =  _Config['jwt']['secret']

jwt = JWTManager(app)

# Append routes
api.add_resource(_signup.UserRegistration, '/signup')
api.add_resource(_login.UserLogin, '/login')

app.run()
