#!flask/bin/python
# Module imports
from flask import Flask, request, jsonify
from utils import functions as _functions
# Routes imports
from routes import public

app = Flask(__name__) # Create http server
app.config["DEBUG"] = _functions.Config['dev']['debug']

# Append routes
@app.route('/', methods=['GET'])
def alive():
    return public.alive()
    
app.run()
