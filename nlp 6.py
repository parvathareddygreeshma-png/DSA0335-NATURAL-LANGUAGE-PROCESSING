words = ["unhappy","redo","disconnected","happiness","quickly","replayed"]

for w in words:
    p = "un" if w.startswith("un") else "re" if w.startswith("re") else "dis" if w.startswith("dis") else ""
    s = "ing" if w.endswith("ing") else "ed" if w.endswith("ed") else "ly" if w.endswith("ly") else "ness" if w.endswith("ness") else ""
    print(w,"|",p,"|",w.strip(p).strip(s),"|",s)
