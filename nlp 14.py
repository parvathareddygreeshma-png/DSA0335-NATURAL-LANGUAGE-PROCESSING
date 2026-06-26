training_data = [
    ("A", "DT"),
    ("dog", "NN"),
    ("barks", "VBZ")
]

hmm = {}

for word, tag in training_data:
    hmm[word] = tag

sentence = "A dog barks"

words = sentence.split()

print("Tagged Sentence:")

for word in words:
    tag = hmm.get(word, "Unknown")
    print(word, "->", tag)
