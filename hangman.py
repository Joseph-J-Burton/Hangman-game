import random
from hangman_art import stages, logo
from hangman_words import word_list
# from replit import clear
from os import system, name


def clear():
    # for windows the name is: 'nt'
    if name == 'nt':
        _ = system('cls')


# TODO 1: future improvements - show a list of guessed letters and number of lives remaining

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported to clear the output between guesses.
    clear()
# TODO 4: It doesn't appear the clear function is working
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
# TODO 2: It may be nice to have what the word was at the end.
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])

# TODO 3: It would be good to add in an end message like "Game over"
