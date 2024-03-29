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

def create_session():
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat


def response(chat, message):
    parameters = {
         "candidate_count": 1,
         "max_output_tokens": 1024,
         "temperature": 0.2,
         "top_p": 0.8,
         "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

        @app.route('/')
def index():
    return render_template('index.html')

@app.route('/palm2', methods=['GET', 'POST'])
def vertex_palm():
    user_input = ""
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        user_input = request.form['user_input']

        print(f"Received user input: {user_input}")
    chat_model = create_session()
    content = response(chat_model,user_input)
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')