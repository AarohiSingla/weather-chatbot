#from rasa_core.channels.facebook import FacebookInput
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.agent import Agent
from flask import Flask
from flask import render_template, jsonify, request
import requests
from urllib.request import urlopen
import json
#from models import *
from responses import *

import random
app = Flask(__name__)



@app.route('/')
def hello_world():

    return render_template('index.html')
    
	

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)

	
