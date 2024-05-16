from flask import Flask, request, jsonify, render_template

from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language='en'):
    """
    Metin çevirisi yapar.
    
    :param text: Çevrilecek metin.
    :param target_language: Hedef dil (varsayılan olarak İngilizce).
    :return: Çevrilmiş metin.
    """
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['input_text']
    translator = Translator()
    translated_text = translator.translate(input_text, dest='en')
    return jsonify({'translated_text': translated_text.text })

if __name__ == "__main__":
    app.run(debug=True)
