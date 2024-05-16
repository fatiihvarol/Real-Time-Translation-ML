import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import joblib
import os

class TranslationModel:
    def __init__(self):
        self.pipeline = Pipeline([
            ('vect', CountVectorizer(max_features=10000, max_df=0.8, min_df=5)),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)),
        ])

    def load_and_train(self, filepath, partial=False):
        data = pd.read_csv(filepath)
        X_train = data['input_text']
        y_train = data['target_text']
        
        if partial and os.path.exists('translation_model.pkl'):
            self.pipeline = joblib.load('translation_model.pkl')
            self.pipeline.fit(X_train, y_train)
        else:
            self.pipeline.fit(X_train, y_train)

    def save_model(self):
        joblib.dump(self.pipeline, 'translation_model.pkl')

if __name__ == "__main__":
    model = TranslationModel()
    
    for i in range(1, 51):
        print(f"Training on part {i}")
        model.load_and_train(f'processed_data_part{i}.csv', partial=True)
        model.save_model()
