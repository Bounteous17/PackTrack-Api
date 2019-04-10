#!flask/bin/python
# Module imports
from flask import Flask, request, jsonify
# Routes imports
from routes import public

app = Flask(__name__) # Create http server
app.config["DEBUG"] = True

# Append routes
@app.route('/', methods=['GET'])
def alive():
    return public.alive()
    
app.run()
