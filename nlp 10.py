sentence = "Anita rapidly solved the challenging problem efficiently"
words = sentence.split()
for word in words:
    if word.endswith("ing"):
        tag = "VBG"
    elif word.endswith("ly"):
        tag = "RB"
    elif word[0].isupper():
        tag = "NNP"
    else:
        tag = "Unknown"
    print(word, "->", tag)
