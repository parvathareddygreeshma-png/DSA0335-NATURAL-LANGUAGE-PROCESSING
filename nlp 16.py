from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "NLP is a branch of AI",
    "Machine learning enables AI systems",
    "Language processing is interesting"
]

query = ["AI systems"]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents + query)

similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

print("Document Ranking:")

scores = similarity[0]

for i, score in enumerate(scores):
    print("D" + str(i+1), "->", score)
