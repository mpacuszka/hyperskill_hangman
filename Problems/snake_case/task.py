from re import findall
word = input()

r = findall('([A-Z])', word)
if r:
    for s in r:
        word = word.replace(s, f"_{s.lower()}")
print(word)