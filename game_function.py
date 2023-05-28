def guess_game():
    secret_word = "elephant"
    guess = ""
    guess_count = 0
    limit_guess = 5
    out_of_guess = False
    print("You have to guess the word correctly within " + str(limit_guess) + " times,"
           "\nbut you will get a hint after you guess wrong " + str(limit_guess // 2) + " time")

    while guess != secret_word and not out_of_guess:
        if guess_count < limit_guess:
            guess = input("Enter your guess: ")
            guess_count += 1
            if guess_count == limit_guess // 2:
                print("Do you a hint (Yes/No)")
                ans = input("Enter your answer: ")
                if ans.lower() == "yes":
                    print("The word start with \"e\" and end with \"t\"")
                else:
                    out_of_guess = True
        else:
            out_of_guess = True
    if out_of_guess:
        print("YOU LOSE !!")
    else:
        print("YOU WIN !!")


def guess_game2():
    secret_word = "lion"
    guess_count = 0
    limit_guess = 4
    print("You have to guess the word correctly within " + str(limit_guess) + " times,"
          "\nbut you will get a hint after you guess wrong " + str(limit_guess // 2) + " time")

    for guess_count in range(limit_guess):
        guess = input("Enter your guess: ")
        if guess == secret_word:
            print("YOU WIN !!")
            return
        elif guess_count == limit_guess // 2 - 1:
            print("Do you need hint (Yes/No)")
            ans = input("Enter answer: ")
            if ans.lower() != "yes":
                print("YOU LOSE!!")
                return
            print("The word start with \"e\" and end with \"t\"")
            guess = input("Enter your guess: ")

    print("YOU LOSE!!")


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
