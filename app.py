from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_definition', methods=['POST'])
def get_definition():
    word = request.form['word']
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Word not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
