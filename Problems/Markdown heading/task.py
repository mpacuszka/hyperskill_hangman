def heading(word, lvl=1):
    return "#" * max(min(lvl, 6), 1) + " " + word
