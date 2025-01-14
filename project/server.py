from flask import Flask, request, jsonify, send_from_directory
from email_chatbot.chatbot import ClassroomChatbot
import os

app = Flask(__name__)
chatbot = ClassroomChatbot(
    cr_name="THANU",
    cr_contact="classchatbot@gmail.com"
)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    response = chatbot.process_query(message)
    if response.startswith('Chatbot: '):
        response = response[9:]  # Remove 'Chatbot: ' prefix
        
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 