from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = "Good Morning"

inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs)

translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("French Translation:", translation)
