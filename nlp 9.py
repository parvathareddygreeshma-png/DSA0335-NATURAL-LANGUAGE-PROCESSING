sentence = ["Smart", "algorithms", "predict", "outcomes", "accurately"]
predicted_tags = ["JJ", "NNS", "VB", "NNS", "RB"]
gold_tags = ["JJ", "NNS", "VB", "NNS", "RB"]
correct = 0
for i in range(len(gold_tags)):
    if predicted_tags[i] == gold_tags[i]:
        correct += 1
accuracy = (correct / len(gold_tags)) * 100
print("Predicted Tags:")
for word, tag in zip(sentence, predicted_tags):
    print(word, "->", tag)
print("\nAccuracy =", accuracy, "%")
