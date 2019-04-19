#!flask/bin/python
# Module imports
from flask import Flask, request, jsonify
from utils import functions as _functions
# Routes imports
import routes as _routes
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
        return __routes.public.alive()
    except:
        return ("")
    
app.run()
