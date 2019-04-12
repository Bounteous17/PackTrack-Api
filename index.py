#!flask/bin/python
# Module imports
from flask import Flask, request, jsonify
from utils import utils as Utils
# Routes imports
from routes import public

app = Flask(__name__) # Create http server
app.config["DEBUG"] = Utils.Config['dev']['debug']

# Append routes
@app.route('/', methods=['GET'])
def alive():
    return public.alive()
    
app.run()
