from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import vertexai
from vertexai.language_models import ChatModel
import os
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "....Add API Key Path ...."
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
PROJECT_ID = "total-entity-409908"  
LOCATION = "us-central1"  
vertexai.init(project=PROJECT_ID, location=LOCATION)