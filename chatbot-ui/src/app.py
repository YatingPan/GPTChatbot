from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to our chatbot!'})

# get request to enter the url /ask
# post request to send the query to the bot

@app.route('/ask', methods=['GET', 'POST'])
def get_bot_response():
    if request.method == 'GET':
        return ask_bot()
    elif request.method == 'POST':
        return ask_bot()

def ask_bot():
    if request.json:
        user_query = request.json.get('query')
        try:
            response = openai.Completion.create(engine="davinci", prompt=user_query, max_tokens=150, temperature=0.7)
            return jsonify({'response': response.choices[0].text.strip()})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No JSON payload provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
