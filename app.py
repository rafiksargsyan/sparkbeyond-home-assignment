from flask import Flask, request, jsonify
from collections import Counter
import re

app = Flask(__name__)

@app.route('/most_common_word', methods=['POST'])
def most_common_word():
    data = request.get_json()
    text = data.get('text', '')

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'\W+', ' ', text).lower()

    # Find the most common word
    words = cleaned_text.split()
    most_common_word = Counter(words).most_common(1)

    return jsonify({'most_common_word': most_common_word[0][0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

