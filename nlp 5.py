bases = ["play","walk","study","stop"]

def check(w):
    for b in bases:
        if w==b or w==b+"s" or w==b+"ed" or w==b+"ing":
            return "Valid",b
    return "Invalid","-"

for w in ["playing","studied","walks","stopping","stop"]:
    print(w,"→",check(w))
