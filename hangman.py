import random
# import subprocess
# import sys
from hangman_art import stages, logo
from hangman_words import word_list
# from replit import clear
from os import system, name
# import sys, subprocess


# def clear_screen():
#     operating_system = sys.platform
#
#     if operating_system == 'win32':
#         subprocess.run('cls', shell=True)
#
#     elif operating_system == 'linux' or operating_system == 'darwin':
#         subprocess.run('clear', shell=True)


def clear():
    # for windows the name is: 'win32'
    if name == 'win32':
        _ = system('cls')


print(logo)
game_is_finished = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = word_length - 1

display = []
letters_used = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    print(f"You have {lives} guesses remaining")
    print(f"Letters already guessed: {letters_used}")
    guess = input("Guess a letter: ").lower()
    letters_used += guess

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
            print(f"You lose. \n The word was: {chosen_word}")
            print("GAME OVER")

    if not "_" in display:
        game_is_finished = True
        print("You win.")
        print("GAME OVER")
    print(stages[lives])


