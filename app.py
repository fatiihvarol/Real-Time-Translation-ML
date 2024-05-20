from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.form.get('input_text', '')
    if input_text:
        translated_text = translator.translate(input_text).text
    else:
        translated_text = "No input provided."
    return jsonify({'translated_text': translated_text})

if __name__ == "__main__":
    app.run(debug=True)
