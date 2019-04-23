#!flask/bin/python
# Module imports
from flask import Flask, request,  abort, jsonify
from utils import functions as _functions
# Routes imports
from routes.public import status as _status, signup as _signup, login as _login
# Models
from models import rest as _rest
# Modules
from modules.db import db as _db

_db.instance()

app = Flask(__name__) # Create http server
_Config = _functions.Config
if _functions.resultError(_Config):
    exit(1)

app.config["DEBUG"] = _Config['dev']['debug']

# Append routes
@app.route('/', methods=['GET'])
def alive():
    try: 
        return _functions.setFlaskResponse(_status.alive())
    except Exception as e:
        return _functions.setFlaskResponse(_functions.setModuleError(payload=e, error="Error into /"))

@app.route('/signup', methods=['POST'])
def signup():
    try:
        if not request.json:
            abort(400)
        return _functions.setFlaskResponse(_signup.signup(request.json))
    except Exception as e:
        return _functions.setFlaskResponse(_functions.setModuleError(payload=e, error="Error into /signup"))

@app.route('/login', methods=['POST'])
def login():
    try:
        if not request.json:
            abort(400)
        return _functions.setFlaskResponse(_login.login(request.json))
    except Exception as e:
        return _functions.setFlaskResponse(_functions.setModuleError(payload=e, error="Error into /login"))


app.run()
