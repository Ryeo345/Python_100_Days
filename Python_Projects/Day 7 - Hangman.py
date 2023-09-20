#Step 1


# Stage 1
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Stage 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# stage 3

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

import random
import sys


sys.path.append("../Python_modules")
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)
# list_size = len(word_list) - 1
# random_idx = random.randint(0, list_size)
# chosen_word = word_list[random_idx]

# word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) # this one line of code is the same as the 3 lines above

lives = 6

# print(f"chosen word: {chosen_word}")

word_length = len(chosen_word)
# display = []
# for letter in chosen_word:
#     display += "_" # same as the append method
# print(display)

display = ["_"] * word_length # faster way to do the above code
print(display)
print(stages[lives])
end_of_game = False
# while "_" in display:
while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in display:
        print(f"You already guessed {guess}")

    for idx in range(word_length):
        letter = chosen_word[idx]
        if letter == guess:
            display[idx] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(" You Lose.")
            print(f"chosen word: {chosen_word}")
        else:
            print(f"You guessed {guess}, that's not in the word. You lost a life.")

    print(display)
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You Win.")





