import sys
sys.path.append("../Python_modules")
from number_art import logo

import random

print(logo)

print("Welcome to the Guessing Game!")
print("Guess a number between 1-100")

num_list = []
for num in range(1, 101):
    num_list.append(num)

target_number = random.choice(num_list)

print(f"The correct number is {target_number}")

def check_guess(guess):
    if guess > target_number:
        return "Too high, guess again"
    elif guess < target_number:
        return "Too low, guess again"
    elif guess == target_number:
        return "That is the correct number. You Win!"
    else:
        return "You ran out of chances, You Lose!"

difficult_level = input("Choose a difficulty level: easy or hard\n")

if difficult_level == "easy":
    chances = 10
elif difficult_level == "hard":
    chances = 5


while chances > 0:
    print(f"You have {chances} chances left")
    player_guess = int(input("Make a guess: "))
    print(check_guess(player_guess))
    if player_guess == target_number:
        chances = 0
    else:
        chances -= 1