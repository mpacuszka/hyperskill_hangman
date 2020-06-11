def what_to_do(instructions):
    magic_word = "Simon says"
    if instructions.startswith(magic_word) or instructions.endswith(magic_word):
        return "I " + instructions.replace(magic_word, "").strip().replace("  ", " ")
    return "I won't do it!"
