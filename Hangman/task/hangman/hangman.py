import random


def game_loop():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    word_copy = [x for x in word]
    word_hashed = [x for x in "-" * len(word)]
    letters_typed = []
    tries = 8
    while tries > 0:
        print("\n" + "".join(word_hashed))
        print("Input a letter: ", end="")
        guess = input()

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not (guess.isascii() and guess.islower()):
            print("It is not an ASCII lowercase letter")
            continue
        if guess not in letters_typed:
            letters_typed.append(guess)
        else:
            print("You already typed this letter")
            continue

        if guess in word_hashed:
            tries -= 1
            print("No improvements")
            continue

        if guess not in word_copy:
            tries -= 1
            print("No such letter in the word")
            continue

        while word_copy.count(guess):
            idx = word_copy.index(guess)
            word_hashed[idx] = guess
            word_copy[idx] = "-"

        if "".join(word_hashed) == word:
            print("\n" + "".join(word_hashed))
            print("You guessed the word!\nYou survived!")
            break
    else:
        print("You are hanged!")


print("H A N G M A N")
while True:
    menu_input = input('Type "play" to play the game, "exit" to quit: ').lower()
    if menu_input == "play":
        game_loop()
    elif menu_input == "exit":
        break
    print('wrong input')
