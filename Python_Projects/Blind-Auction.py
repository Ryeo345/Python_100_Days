import sys

sys.path.append("../Python_modules")

from auction_art import logo
print(logo)

bids = {}

bidding_finished = False

def find_the_highest_bidder(bidding_record):
    highest_bid = 0
    for name, price in bidding_record.items():
        if price > highest_bid:
            winner = name
            highest_bid = price
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name? \n ")
    price = int(input("What is your bid? \n$"))
    bids[name] = price
    should_continue = input("Are there anymore bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_the_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 100)





