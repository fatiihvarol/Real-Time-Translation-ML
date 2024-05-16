from flask import Flask, request, jsonify, render_template
import joblib

class Translator:
    def __init__(self):
        self.model = joblib.load('translation_model.pkl')

    def translate(self, input_text):
        return self.model.predict([input_text])[0]

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    translated_text = translator.translate(input_text)
    return jsonify({'translated_text': translated_text})

if __name__ == "__main__":
    app.run(debug=True)
