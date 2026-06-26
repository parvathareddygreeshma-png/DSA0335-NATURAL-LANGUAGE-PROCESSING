import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

words = ["Cats", "running", "played"]

lem = WordNetLemmatizer()

for w in words:
    print(w, "→", lem.lemmatize(w.lower()))
