import joblib

class Translator:
    def __init__(self):
        self.model = joblib.load('translation_model.pkl')

    def translate(self, input_text):
        return self.model.predict([input_text])[0]
