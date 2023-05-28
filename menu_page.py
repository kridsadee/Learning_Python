from game_function import guess_game
from game_function import guess_game2
from game_function import translate_game

print("Welcome to the Game Menu!")
game = ["guess game1", "guess game2", "translation"]
for index, name in enumerate(game, 1):
    print(index, name)

choice = input("Enter your choice: ")

if choice == "1":
    guess_game()
elif choice == "2":
    guess_game2()
elif choice == "3":
    phrase = input("Enter your phrase: ")
    print(translate_game(phrase))
else:
    print("Invalid cho ice. Please try again.")
