from flask import Flask, jsonify
from flask_cors import CORS   # 👈 ADD

app = Flask(__name__)
CORS(app)  # 👈 ENABLE

my_dictionary = {
    "mon": {
        "definition": "Mon language example",
        "phonetic": "mon",
        "partOfSpeech": "noun"
    },
    "hello": {
        "definition": "Grating",
        "phonetic": "Halo",
        "partOfSpeech": "noun"
    },
    "mingalar": {
        "definition": "မင်္ဂလာပါ",
        "phonetic": "ming-ga-la",
        "partOfSpeech": "greeting"
    }
}

@app.route('/word/<w>')
def get_word(w):
    word = w.lower()

    if word in my_dictionary:
        return jsonify(my_dictionary[word])
    else:
        return jsonify({"error": "Word not found"}), 404

app.run(debug=True)