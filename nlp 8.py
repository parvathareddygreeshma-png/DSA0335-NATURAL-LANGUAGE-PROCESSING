corpus = "Deep learning models are powerful. Learning models improve accuracy."
corpus = corpus.lower().replace(".", "")
words = corpus.split()
unigram = {}
bigram = {}
for i in range(len(words) - 1):
    w1 = words[i]
    w2 = words[i + 1]
    unigram[w1] = unigram.get(w1, 0) + 1
    bigram[(w1, w2)] = bigram.get((w1, w2), 0) + 1
sentence = "deep learning models are effective"
test_words = sentence.split()
probability = 1
for i in range(len(test_words) - 1):
    w1 = test_words[i]
    w2 = test_words[i + 1]
    bigram_count = bigram.get((w1, w2), 0)
    unigram_count = unigram.get(w1, 0)
    if unigram_count == 0:
        probability = 0
        break
    probability *= (bigram_count / unigram_count)
print("Sentence Probability =", probability)
