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
    },
    "computer": {
        "definition":"an electronic device that accepts data, processes it, and produces information.",
        "phonetic": "kum-pyu-ter",
        "partOfSpeech": "noun"
    },
    "apple": {
        "definition": "It is a fruit",
        "phonetic": "ap",
        "partOfSpeech": "haha"
    }

@app.route('/word/<w>')
def get_word(w):
    word = w.lower()

    if word in my_dictionary:
        return jsonify(my_dictionary[word])
    else:
        return jsonify({"error": "Word not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
