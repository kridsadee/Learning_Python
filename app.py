from game_function import guess_game
from game_function import translate_game


print("Welcome to the Game Menu!")
print("1. Guessing Game")
print("2. Translation Game")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    guess_game()
elif choice == "2":
    phrase = input("Enter your phrase: ")
    print(translate_game(phrase))
else:
    print("Invalid choice. Please try again.")