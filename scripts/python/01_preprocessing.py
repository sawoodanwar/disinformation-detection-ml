# Disinformation Detection | Script 01: Preprocessing
# Author: Sawood Anwar

import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()

# df = pd.read_csv('data/posts.csv')
# df['clean_text'] = df['text'].apply(clean_text)
# vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
# X = vectorizer.fit_transform(df['clean_text'])
# y = df['label']
print('Preprocessing script ready.')
