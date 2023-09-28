# add the logos and data from the other modules

import sys
sys.path.append("../Python_modules")
from Higher_lower_art import logo, vs
from Higher_lower_game_data import data

print(logo)

# randomize the data that is being compared

# get randint for random index
import random
def get_random_star(data):
    random_star = random.choice(data)
    return random_star

def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"

continue_game = True
score = 0
while continue_game:
    account_A = get_random_star(data)

    # output the print statement with the object data
    print(f"Compare A: {account_A['name']}, a {account_A['description']}, from {account_A['country']}.")

    # print vs
    print(vs)

    account_B = get_random_star(data)
    print(f"Against B: {account_B['name']}, a {account_B['description']}, from {account_B['country']}.")

    #take a guess as an input
    guess = input("Who has more followers? Type 'A' or 'B' ")

    if guess == compare(account_A, account_B):
        score += 1
        print(f"You are correct. Current Score: {score}")
    else:
        print(f"You are wrong. You Lose. Current Score: {score}")
        continue_game = False




