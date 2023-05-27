def guess_game():
    secret_word = "lion"
    guess = ""
    guess_count = 0
    limit_guess = 4
    out_of_guess = False
    while guess != secret_word and not out_of_guess:
        if guess_count < limit_guess:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_guess = True

    if out_of_guess:
        print("Out of Guess, YOU LOST!!")
    else:
        print("You Win!!")


def translate_game(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
