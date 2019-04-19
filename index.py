#!flask/bin/python
# Module imports
from flask import Flask, request, jsonify
from utils import functions as _functions
# Routes imports
from routes import public as _public
# Models
from models import rest as _rest

app = Flask(__name__) # Create http server
_Config = _functions.Config
if _functions.resultError(_Config):
    exit(1)

app.config["DEBUG"] = _Config['dev']['debug']

# Append routes
@app.route('/', methods=['GET'])
def alive():
    try:
        rAlive = _public.alive()
        if _functions.resultError(rAlive):
            return rAlive.flaskResp()
        return rAlive
    except Exception as e:
        error = "Error into /"
        newError = _functions.setModuleError(payload=e, error=error)
        return newError.flaskResp()
    
app.run()
