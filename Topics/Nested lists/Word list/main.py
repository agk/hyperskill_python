text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
# if len(word) <= n print(word)
n = int(input())
els = [el for t in text for el in t if len(el) <= n]
print(els)