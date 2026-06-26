words = ["Cats","dogs","played","running","studies","writes","boxes","talked"]

def analyze(w):
    if w.endswith("ies"): return w[:-3]+"y","Plural"
    elif w.endswith("ing"): return w[:-3],"Present Participle"
    elif w.endswith("ed"): return w[:-2],"Past"
    elif w.endswith("es"): return w[:-2],"Plural"
    elif w.endswith("s"): return w[:-1],"3rd Person/Plural"
    return w,"Root"

for w in words:
    r,t = analyze(w.lower())
    print(w, "|", r, "|", t)
