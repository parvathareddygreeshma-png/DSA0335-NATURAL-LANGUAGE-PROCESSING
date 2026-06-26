from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["researchers","analyzing","collected","studies"]

ps = PorterStemmer()
lm = WordNetLemmatizer()

for w in words:
    print(w,"|",ps.stem(w),"|",lm.lemmatize(w))
